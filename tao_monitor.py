"""
TAO Subnet Monitor
==================
Polls Bittensor on-chain data hourly, calculates GBP value of all positions,
and POSTs a snapshot to the 10x dashboard.

PM2 setup:
  pm2 start ~/Desktop/TAO_WALLET/tao_monitor.py --interpreter python3 \
    --cron "0 * * * *" --no-autorestart --name tao-monitor

Manual run:
  python3 ~/Desktop/TAO_WALLET/tao_monitor.py
"""

import asyncio
import json
import logging
import os
import requests
import bittensor

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# =============================================================================
# CONFIG
# =============================================================================

DASHBOARD_URL = "https://10x-app-production.up.railway.app"
COLDKEY = os.getenv("COLDKEY", "")
COST_BASIS_GBP = float(os.getenv("COST_BASIS_GBP", "0"))

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
# MAIN
# =============================================================================


async def run():
    logger.info("=== TAO Monitor snapshot ===")

    # TAO price
    try:
        r = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": "bittensor", "vs_currencies": "gbp"},
            timeout=10,
        )
        tao_price = float(r.json()["bittensor"]["gbp"])
        logger.info(f"TAO price: £{tao_price:.2f}")
    except Exception as e:
        logger.error(f"Could not fetch TAO price: {e}")
        return

    # On-chain positions
    sub = bittensor.AsyncSubtensor(network="finney")
    await sub.initialize()

    positions = []
    for netuid, (name, pos_type, validator_hotkey) in SUBNET_VALIDATORS.items():
        try:
            result = await sub.get_stake_for_coldkey_and_hotkey(
                COLDKEY, validator_hotkey
            )
            s = result.get(netuid)
            tokens = float(s.stake.tao) if s else 0.0
            emission = float(s.emission.tao) if s and s.emission else 0.0

            if tokens == 0:
                continue

            if pos_type == "root":
                price_tao = 1.0
                tao_value = tokens
            else:
                subnet_price = await sub.get_subnet_price(netuid)
                price_tao = float(subnet_price.tao) if subnet_price else 0.0
                tao_value = tokens * price_tao

            value_gbp = tao_value * tao_price
            positions.append(
                {
                    "netuid": netuid,
                    "name": name,
                    "type": pos_type,
                    "alphaTokens": round(tokens, 6),
                    "priceTao": round(price_tao, 8),
                    "taoValue": round(tao_value, 4),
                    "valueGbp": round(value_gbp, 2),
                    "emissionAlpha": round(emission, 6),
                }
            )
            logger.info(f"  SN{netuid} {name}: {tokens:.4f} = £{value_gbp:.2f}")

        except Exception as e:
            logger.error(f"  SN{netuid} {name} error: {e}")

    await sub.substrate.close()

    if not positions:
        logger.warning("No positions found")
        return

    total_value_gbp = sum(p["valueGbp"] for p in positions)
    pnl_gbp = total_value_gbp - COST_BASIS_GBP
    logger.info(f"Total: £{total_value_gbp:.2f} | PnL: £{pnl_gbp:+.2f}")

    payload = {
        "taoPrice": tao_price,
        "totalValueGbp": round(total_value_gbp, 2),
        "costBasisGbp": COST_BASIS_GBP,
        "pnlGbp": round(pnl_gbp, 2),
        "positions": positions,
    }

    try:
        resp = requests.post(
            f"{DASHBOARD_URL}/api/tao-snapshot", json=payload, timeout=15
        )
        resp.raise_for_status()
        logger.info("✅ Snapshot saved to dashboard")
    except Exception as e:
        logger.error(f"Failed to POST snapshot: {e}")
        with open("/tmp/tao_snapshot_latest.json", "w") as f:
            json.dump(payload, f, indent=2)
        logger.info("Saved to /tmp/tao_snapshot_latest.json as fallback")


if __name__ == "__main__":
    asyncio.run(run())
