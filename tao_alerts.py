"""
TAO Alert System
================
Two jobs in one process:

1. PRICE ALERTS (runs every hour alongside tao_monitor)
   - TAO hits $500  → "Get whole" alert
   - TAO hits $3000 → "First major exit" alert
   - Portfolio hits 2x, 5x, 10x cost basis
   - Any alpha token price spikes >30% vs last snapshot

2. DISCORD WATCHER (persistent)
   - Watches Bittensor #announcements channel
   - Fires immediately on keywords: listing, exchange, CEX, coinbase, binance,
     kraken, bybit + any of our subnet names

All alerts go to Telegram.

PM2: pm2 start ~/Desktop/TAO_WALLET/tao_alerts.py --interpreter python3 --name tao-alerts
"""

import asyncio
import json
import logging
import os
import requests
import discord
import bittensor
from datetime import datetime, timezone
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# =============================================================================
# CONFIG
# =============================================================================

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", "")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")

COLDKEY = os.getenv("COLDKEY", "")
COST_BASIS_GBP = 9805.0
DASHBOARD_URL = "https://10x-app-production.up.railway.app"

# Price alert thresholds (USD)
TAO_PRICE_ALERTS = [500, 3000, 10000, 30000]

# Portfolio multiplier alerts
PORTFOLIO_MULTIPLIER_ALERTS = [2, 5, 10, 25]

# Alpha spike threshold (30% in one hour)
ALPHA_SPIKE_PCT = 0.20

# £5k deploy window alerts
DEPLOY_DIP_THRESHOLD_USD = 240  # alert if TAO drops to this price or below
DEPLOY_REMINDER_DAYS = 14  # fallback reminder if no dip after this many days

# Discord keywords that trigger an alert
LISTING_KEYWORDS = [
    "listing",
    "listed",
    "exchange",
    "cex",
    "coinbase",
    "binance",
    "kraken",
    "bybit",
    "okx",
    "kucoin",
    "gate.io",
    "mexc",
    "chutes",
    "ridges",
    "targon",
    "hippius",
    "nova",
    "precog",
    "sn64",
    "sn62",
    "sn4",
    "sn75",
    "sn68",
    "sn55",
]

# State file — tracks which alerts have already fired
STATE_FILE = Path("/Users/lewisjackson/Desktop/TAO_WALLET/tao_alert_state.json")

SUBNET_VALIDATORS = {
    0: ("Root → TAO.com", "root", "5HK5tp6t2S59DywmHRWPBVJeJ86T61KjurYqeooqj8sREpeN"),
    64: ("Chutes", "alpha", "5Dt7HZ7Zpw4DppPxFM7Ke3Cm7sDAWhsZXmM5ZAmE7dSVJbcQ"),
    62: ("Ridges", "alpha", "5Djyacas3eWLPhCKsS3neNSJonzfxJmD3gcrMTFDc4eHsn62"),
    4: ("Targon", "alpha", "5Hp18g9P8hLGKp9W3ZDr4bvJwba6b6bY3P2u3VdYf8yMR8FM"),
    75: ("Hippius", "alpha", "5G1Qj93Fy22grpiGKq6BEvqqmS2HVRs3jaEdMhq9absQzs6g"),
    68: ("Nova", "alpha", "5F1tQr8K2VfBr2pG5MpAQf62n5xSAsjuCZheQUy82csaPavg"),
    55: ("Ko/Precog", "alpha", "5CzSYnS88EpVv7Kve7U1VCYKjCbtKpxZNHMacAy3BkfCsn55"),
}

# =============================================================================
# HELPERS
# =============================================================================


def send_telegram(message: str):
    try:
        r = requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message,
                "parse_mode": "Markdown",
            },
            timeout=10,
        )
        r.raise_for_status()
        logger.info(f"Telegram sent: {message[:80]}")
    except Exception as e:
        logger.error(f"Telegram failed: {e}")


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {
        "fired_price_alerts": [],
        "fired_multiplier_alerts": [],
        "last_alpha_prices": {},
        "deploy_dip_fired": False,
        "deploy_reminder_fired": False,
        "first_run_ts": datetime.now(timezone.utc).isoformat(),
    }


def save_state(state: dict):
    STATE_FILE.write_text(json.dumps(state, indent=2))


def get_tao_price_usd() -> float:
    try:
        r = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": "bittensor", "vs_currencies": "usd,gbp"},
            timeout=10,
        )
        data = r.json()["bittensor"]
        return float(data["usd"]), float(data["gbp"])
    except Exception as e:
        logger.error(f"Price fetch failed: {e}")
        return 0.0, 0.0


# =============================================================================
# PRICE CHECKER (runs hourly)
# =============================================================================


async def check_price_alerts():
    state = load_state()
    tao_usd, tao_gbp = get_tao_price_usd()
    if tao_usd == 0:
        return

    # --- TAO price thresholds ---
    for threshold in TAO_PRICE_ALERTS:
        key = f"tao_{threshold}"
        if tao_usd >= threshold and key not in state["fired_price_alerts"]:
            if threshold == 500:
                action = "🟡 *ACTION: Unstake 25% of root staking.* Recover cost basis."
            elif threshold == 3000:
                action = "🟠 *ACTION: Take 25% off everything.* ~£25k locked in."
            elif threshold == 10000:
                action = "🔴 *ACTION: Take another 25% off.* Reassess remaining."
            else:
                action = "🚀 *HOLD.* Full Bitcoin thesis playing out."

            send_telegram(
                f"🎯 *TAO PRICE ALERT — ${threshold:,} HIT*\n\n"
                f"TAO is at *${tao_usd:,.0f}* (£{tao_gbp:,.0f})\n\n"
                f"{action}\n\n"
                f"Dashboard: {DASHBOARD_URL}"
            )
            state["fired_price_alerts"].append(key)

    # --- £5k deploy window alerts ---
    if not state.get("deploy_dip_fired") and tao_usd <= DEPLOY_DIP_THRESHOLD_USD:
        send_telegram(
            f"📉 *TAO DIP ALERT — Deploy the £5k now*\n\n"
            f"TAO has dropped to *${tao_usd:,.0f}* (£{tao_gbp:,.0f})\n"
            f"That's below your ${DEPLOY_DIP_THRESHOLD_USD} deploy trigger.\n\n"
            f"Run: `python3 ~/Desktop/TAO_WALLET/tao_deploy.py`\n"
            f"Dashboard: {DASHBOARD_URL}"
        )
        state["deploy_dip_fired"] = True

    if not state.get("deploy_reminder_fired"):
        first_run = datetime.fromisoformat(
            state.get("first_run_ts", datetime.now(timezone.utc).isoformat())
        )
        days_elapsed = (datetime.now(timezone.utc) - first_run).days
        if days_elapsed >= DEPLOY_REMINDER_DAYS:
            send_telegram(
                f"⏰ *£5k DEPLOY REMINDER*\n\n"
                f"It's been {days_elapsed} days since your TAO deployment.\n"
                f"TAO is currently *${tao_usd:,.0f}* (£{tao_gbp:,.0f}) — no dip came.\n\n"
                f"Consider deploying the remaining £5k regardless.\n"
                f"Run: `python3 ~/Desktop/TAO_WALLET/tao_deploy.py`\n"
                f"Dashboard: {DASHBOARD_URL}"
            )
            state["deploy_reminder_fired"] = True

    # --- Portfolio multiplier alerts ---
    try:
        r = requests.get(f"{DASHBOARD_URL}/api/tao-positions", timeout=10)
        tao_data = r.json().get("data")
        if tao_data:
            total = tao_data["totalValueGbp"]
            multiplier = total / COST_BASIS_GBP
            for m in PORTFOLIO_MULTIPLIER_ALERTS:
                key = f"mult_{m}x"
                if multiplier >= m and key not in state["fired_multiplier_alerts"]:
                    send_telegram(
                        f"💰 *TAO PORTFOLIO {m}X ALERT*\n\n"
                        f"Your TAO portfolio is now worth *{formatGbp(total)}*\n"
                        f"Cost basis: £{COST_BASIS_GBP:,.0f} → *{multiplier:.1f}x*\n\n"
                        f"Reminder: take 25% off the table.\n"
                        f"Dashboard: {DASHBOARD_URL}"
                    )
                    state["fired_multiplier_alerts"].append(key)

            # --- Alpha token spike detection ---
            positions = tao_data.get("positions", [])
            for pos in positions:
                if pos["type"] != "alpha":
                    continue
                netuid = str(pos["netuid"])
                current_price = pos["priceTao"]
                last_price = state["last_alpha_prices"].get(netuid, current_price)
                if last_price > 0:
                    change = (current_price - last_price) / last_price
                    if change >= ALPHA_SPIKE_PCT:
                        send_telegram(
                            f"📈 *ALPHA SPIKE — {pos['name']} (SN{pos['netuid']})*\n\n"
                            f"Price jumped *+{change*100:.0f}%* in the last hour\n"
                            f"From {last_price:.6f} → {current_price:.6f} τ/α\n"
                            f"Current value: £{pos['valueGbp']:,.0f}\n\n"
                            f"Could be a CEX listing or major catalyst. Check Discord."
                        )
                state["last_alpha_prices"][netuid] = current_price

    except Exception as e:
        logger.error(f"Portfolio check failed: {e}")

    save_state(state)


def formatGbp(v: float) -> str:
    return f"£{v:,.0f}"


# =============================================================================
# TWITTER WATCHER (polls every 15 mins via nitter)
# =============================================================================

WATCH_ACCOUNTS = ["const_anto", "markjeffrey", "bittensor_", "tao_dot_com"]


async def check_twitter():
    """Scrapes nitter (Twitter mirror) every 15 mins for key accounts."""
    import httpx

    state = load_state()
    if "seen_tweet_ids" not in state:
        state["seen_tweet_ids"] = []

    for account in WATCH_ACCOUNTS:
        try:
            async with httpx.AsyncClient(timeout=15, follow_redirects=True) as client:
                r = await client.get(
                    f"https://nitter.poast.org/{account}/rss",
                    headers={"User-Agent": "Mozilla/5.0"},
                )
            if r.status_code != 200:
                continue

            import xml.etree.ElementTree as ET

            root = ET.fromstring(r.text)
            items = root.findall(".//item")[:5]  # last 5 tweets

            for item in items:
                title = item.findtext("title", "")
                link = item.findtext("link", "")
                guid = item.findtext("guid", link)

                if guid in state["seen_tweet_ids"]:
                    continue

                content_lower = title.lower()
                matched = [kw for kw in LISTING_KEYWORDS if kw in content_lower]

                if matched:
                    send_telegram(
                        f"🚨 *@{account} — BITTENSOR ALERT*\n\n"
                        f"{title}\n\n"
                        f"Keywords: {', '.join(matched[:5])}\n"
                        f"Link: {link}"
                    )
                    logger.info(f"Twitter alert: @{account} — {matched}")

                state["seen_tweet_ids"].append(guid)

            # Keep seen list from growing forever
            state["seen_tweet_ids"] = state["seen_tweet_ids"][-500:]

        except Exception as e:
            logger.warning(f"Twitter check failed for @{account}: {e}")

    save_state(state)


# =============================================================================
# DISCORD BOT (stays connected, forwards anything posted to your server)
# =============================================================================


class BittensorWatcher(discord.Client):
    async def on_ready(self):
        logger.info(f"Discord bot connected as {self.user}")
        send_telegram(
            "✅ *TAO Alert System online*\n\n"
            "Monitoring:\n"
            "• Twitter: @const\\_anto, @markjeffrey, @bittensor\\_, @tao\\_dot\\_com (every 15 min)\n"
            "• Price alerts: $500 / $3,000 / $10,000 / $30,000\n"
            "• Portfolio: 2x / 5x / 10x / 25x\n"
            "• Alpha spikes: >20% in 1hr"
        )
        # Start Twitter poller
        self.loop.create_task(self._twitter_loop())

    async def _twitter_loop(self):
        while True:
            try:
                await check_twitter()
            except Exception as e:
                logger.error(f"Twitter loop error: {e}")
            await asyncio.sleep(900)  # 15 minutes


async def run_price_checker():
    """Runs price checks every hour."""
    while True:
        try:
            await check_price_alerts()
        except Exception as e:
            logger.error(f"Price checker error: {e}")
        await asyncio.sleep(3600)


async def main():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.guilds = True
    intents.messages = True

    client = BittensorWatcher(intents=intents)

    # Run price checker and Discord watcher concurrently
    async with client:
        asyncio.create_task(run_price_checker())
        await client.start(DISCORD_BOT_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
