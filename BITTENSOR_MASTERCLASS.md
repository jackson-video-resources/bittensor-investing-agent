# The Bittensor Masterclass: How I Used Claude Code to Build a Fully Automated AI Investment System

---

> ⚠️ **IMPORTANT — READ BEFORE CONTINUING**
>
> This document is a **technical tutorial**, not financial advice. Nothing here constitutes a recommendation to buy, sell, or hold any asset. Cryptocurrency investments — including TAO and subnet alpha tokens — are highly speculative, illiquid, and can result in total loss of capital. Past performance (including any results mentioned in the accompanying video) is not indicative of future results and should not be used as a basis for investment decisions. Any figures referenced — including portfolio performance over short time periods — reflect one individual's experience under specific market conditions and are not representative of typical outcomes.
>
> Before investing in any cryptocurrency, consult a qualified financial adviser. Be aware that staking rewards and alpha token positions may constitute taxable events in your jurisdiction — consult a tax professional before proceeding.
>
> This tutorial is designed to help you build technical infrastructure. The investment decisions you make with that infrastructure are entirely your own responsibility.

---

## VIDEO OPEN — Hook & Framing

> *Re-root the intro here. Don't go straight into the masterclass — set up why this video exists first.*

### Front-load CTA (say this before anything else)

- "Before we get into anything — you can do this whole thing yourself in **just 10 minutes**."
- "Click the link in the description. I'll give you a free document. There's no sales pitch — I just want to make you a ton of money."
- "Once you've done that, it's probably worth staying for the full video so you actually understand what's going on."

---

### The Hook (lead with this)

**The problem:**
- Bittensor is on the verge of absolutely exploding
- The way it's set up — with subnets — creates a massive moat between the everyday person and the opportunity
- You either need insane knowledge of how subnets work, how AI systems interact, how the validator economics function… and it gets intense fast
- Most people hit that wall and walk away

**The bridge:**
- We're living in a world where AI can collapse the time it takes to understand all of this
- You don't even have to learn it — you just have to learn how to tell AI what to do
- That's exactly what this video is

**The stakes:**
- This tutorial could be the difference between you building generational wealth this year — or not
- Don't say "2026" — say "this year"
- Close with: *"Trade 10 minutes for generational wealth. Let's get into it."*

---

### Video Structure (what comes after the open)

1. **Architecture overview** — what the system does, how it executes, where it executes, why it makes decisions in certain places, where the data comes from
2. **Build it live** — click by click, every step on screen
3. **Close** — reveal the free document in the description. No upsell. No pitch. Just give it away.

> *Framing for the close: "There's a document in the description. For free. No sales. I just want to make you a load of money."*

---

## Three Things You're Walking Away With Today

**1. A fully built, automated Bittensor investment strategy — set up entirely using AI.** Not a theory. Not a framework to figure out later. An actual working system: subnets, allocations, entry strategies, exit strategies, and automated alerts that tell you exactly when to act. Built for you, by AI, on your computer.

**2. A live dashboard that tracks every position in real time.** Your total portfolio value in GBP, your P&L against your cost basis, every subnet position updated every hour — visible anywhere, on any device. You'll never have to manually check anything again.

**3. A way to do all of this in the next 10 minutes.** There's a link in the description to a single free document. Drop it into Claude Code, answer a few questions, and it builds your entire system for you — every script, every alert, every dashboard route. Done. No coding. No technical knowledge required.

> **Note on the accompanying video:** The portfolio figures shown in the video reflect a specific period of market movement and should not be treated as a typical or repeatable outcome. Cryptocurrency markets are highly volatile — positions can move significantly in both directions. The system described here is a monitoring and automation tool; it does not guarantee returns.
>
> The 10x Challenge referenced in the video is a personal goal with real capital at risk. It is not a managed fund and viewers should not make investment decisions based on its performance.

---

## Why This Is the Most Important Tutorial I've Ever Made

In the early 2010s a small group of people understood something the rest of the world didn't.

They understood Bitcoin wasn't just a technology. It was a bet on decentralised, permissionless, unstoppable money. The people who acted on that thesis early — and held — saw extraordinary returns.

We may be at a similarly early moment. Only this time it's not money being decentralised.

**It's intelligence.**

Bittensor (TAO) is building a decentralised AI network. Every AI model, every dataset, every GPU — competing in an open market. No single company controls it. And it is compounding in capability the same way the internet compounded in the 1990s.

Whether that thesis plays out is genuinely uncertain. Crypto is a high-risk asset class. But the gap between awareness and the opportunity may be significant — and this tutorial gives you the tools to participate if you choose to.

**From zero — no wallet, no TAO, no code — to a fully operational, automated investment system. Built with Claude Code. Running on your computer.**

---

## What You'll Need Before We Start

> **Platform note:** This tutorial is written for **macOS**. The core scripts will work on Linux with minor path adjustments. Windows users will need WSL2 (Windows Subsystem for Linux) — the caffeinate command and some path conventions will not work natively on Windows.

| Item | What it is | Cost |
|------|-----------|------|
| **Computer** | Mac preferred (Linux works; Windows requires WSL2) | You have one |
| **Claude Code** | Anthropic's AI coding assistant — runs in your terminal | Free to start |
| **Python 3.10+** | Programming language — check with `python3 --version` | Free |
| **Node.js 18+** | Required for PM2 — check with `node --version` | Free |
| **PM2** | Background process manager — install separately (see below) | Free |
| **Caleb & Brown** | UK OTC crypto broker (or Coinbase) | Free to open |
| **Telegram** | For alerts to your phone | Free |
| **CoinGecko API key** | Free tier available — recommended for reliability | Free |
| **Capital** | Whatever you're committing. Works at any size. | Your call |

---

## PART 1: Understanding the Strategy

### What is Bittensor?

Bittensor is a decentralised network where AI models compete to produce the best outputs. Think of it like a marketplace for intelligence. Miners run AI models. Validators score them. The best miners earn TAO — the network's native token — as a reward.

The analogy that clicked for me: **Bitcoin incentivises people to secure a ledger. Bittensor incentivises people to improve AI.**

The network is divided into **subnets** — each one focused on a specific AI task. Text generation. Image generation. Financial prediction. Protein folding. Each subnet has its own token called an **alpha token**.

### The dTAO Upgrade — Why Now

In early 2025 Bittensor upgraded to **dTAO**. Before this upgrade, all TAO emissions went to one central pool. After dTAO, emissions flow to individual subnets based on market demand. It's the moment the network became truly decentralised.

This created two ways to invest:

**Root staking** — Stake your TAO directly with a validator. Earn TAO emissions passively. Think of this as the steady foundation of your portfolio. Lower risk relative to alpha tokens, but still a high-risk crypto asset.

**Alpha token staking** — Stake into specific subnets and receive that subnet's alpha token. Higher risk and higher volatility. Alpha tokens are priced against TAO via subnet-specific bonding curves — their GBP value depends on both the alpha/TAO exchange rate and the TAO/GBP rate. These are early-stage, illiquid assets.

### A Note on Validator Hotkeys

The hotkeys listed in this document were valid at time of writing. Validators can migrate, deregister, or be replaced. **Before deploying capital, verify each hotkey is still active on [taostats.io](https://taostats.io).** The deployment script will preview exactly where your capital is going — read that preview carefully before confirming.

### Who is Mark Jeffrey?

Mark Jeffrey is a researcher in the Bittensor ecosystem and a partner at Stillcore Capital, a fund focused on TAO. The allocation framework used here is informed by his publicly available research and podcast appearances. This is not an endorsement of his fund or its performance, and the allocation below reflects one interpretation of that research — not a direct copy of any fund's positions.

### The Allocation

| Position | Subnet | What it does | Allocation |
|----------|--------|-------------|-----------|
| Root staking (TAO.com) | netuid 0 | Base TAO yield | ~50% |
| Chutes | SN64 | AI inference marketplace | ~16.5% |
| Ridges | SN62 | Financial prediction | ~11% |
| Targon | SN4 | Text generation / compute | ~9.5% |
| Hippius | SN75 | Decentralised cloud | ~7% |
| Nova | SN68 | Data pipelines | ~3.5% |
| Ko/Precog | SN55 | Market prediction | ~2.5% |

**This allocation is not a recommendation.** It represents one approach based on publicly available research. You should form your own view before committing capital. A more conservative starting point for new investors is to hold TAO only (root staking or simply holding) until you have a deeper understanding of individual subnets.

### The Exit Strategy

This is intended as a long-term position. Having a pre-planned exit removes emotion from decisions.

| TAO Price (USD) | Action |
|-----------------|--------|
| $500 | Consider taking 25% off root staking — recover cost basis |
| $3,000 | Consider taking 25% off everything |
| $10,000 | Consider taking another 25% off |
| $30,000+ | Reassess based on market conditions at the time |

**No single exit rule is right for everyone.** Adjust these thresholds to match your own financial situation and risk tolerance.

### Tax Considerations

Staking rewards, alpha token receipts, and token swaps may constitute taxable events in your jurisdiction. Keep records of all transactions, including stake amounts, dates, and values at time of transaction. Consult a tax professional before proceeding — this is especially important if you are in a jurisdiction with specific crypto reporting requirements (UK, US, EU, Australia).

---

## PART 2: Installing Dependencies

Install everything before building the scripts. Run these in order.

### Install Node.js (if not already installed)

Download from [nodejs.org](https://nodejs.org) — LTS version. Verify:

```bash
node --version   # should show v18 or higher
npm --version
```

### Install Python packages

```bash
pip3 install bittensor requests aiohttp httpx python-dotenv
```

Verify bittensor installed:

```bash
python3 -c "import bittensor; print(bittensor.__version__)"
```

### Install PM2

```bash
npm install -g pm2
```

Verify:

```bash
pm2 --version
```

### Install Claude Code

```bash
npm install -g @anthropic/claude-code
```

Follow the login flow — you'll need a free Anthropic account. Once installed:

```bash
claude
```

### How to Give Claude Code Instructions

Claude Code works best when you give it **context and intent**. Always start a session by navigating to the folder where you want to work:

```bash
cd ~/Desktop/TAO_WALLET
claude
```

Everything Claude Code creates will land in that folder.

---

## PART 3: Installing Bittensor CLI

```bash
pip3 install bittensor
```

Verify it worked:

```bash
btcli --version
```

You should see version 9.x or higher.

---

## PART 4: Creating Your Wallet

Your Bittensor wallet has two parts:

- **Coldkey** — Your main wallet address. This is where your TAO lives. Think of it like your bank account number.
- **Hotkey** — Used for staking operations internally.

Create your wallet:

```bash
btcli wallet create --wallet-name tao_main
```

You'll be asked to set a password. Choose something strong.

Then — and this is critical — **your 12-word seed phrase will appear on screen.** This is the master key to your wallet. If you lose it, your TAO is gone forever. If someone else gets it, your TAO is gone forever.

### Protect Your .env File

When Claude Code builds your scripts, it will create an `.env` file containing sensitive values: your wallet address, Telegram credentials, and cost basis. Treat this file like cash.

**Minimum protections:**
- Never share it with anyone
- Never upload it to GitHub, iCloud, Google Drive, or any cloud service
- Never screenshot it and store it in your photo library
- Store a backup copy on an encrypted USB drive in a safe location

**Better options for sensitive values:**
- Use a password manager (1Password, Bitwarden) to store your seed phrase and Telegram token
- Consider using macOS Keychain for the Telegram bot token instead of plaintext .env storage

### Create a .gitignore Immediately

If you ever initialise a git repository in this folder (even accidentally), your `.env` could be committed and pushed to a remote. Create a `.gitignore` now:

```bash
cd ~/Desktop/TAO_WALLET
echo ".env" >> .gitignore
echo "*.log" >> .gitignore
echo "tao_alert_state.json" >> .gitignore
```

### Create Your .env File

Tell Claude Code:

```
Create a .env file in ~/Desktop/TAO_WALLET/ with the following entries:
WALLET_NAME=tao_main
COLDKEY_ADDRESS=[your coldkey address]
COST_BASIS_GBP=10000
TELEGRAM_BOT_TOKEN=[your token]
TELEGRAM_CHAT_ID=[your chat ID]
COINGECKO_API_KEY=[your key — see below]
DASHBOARD_URL=[your dashboard URL]
```

### Get a CoinGecko API Key (Recommended)

The free CoinGecko tier has rate limits that can cause silent failures in the price checker. A free API key raises these limits significantly and enables proper error handling.

1. Go to [coingecko.com/en/api](https://www.coingecko.com/en/api)
2. Create a free account
3. Generate a Demo API key
4. Add it to your `.env` as `COINGECKO_API_KEY`

---

## PART 5: Buying TAO and Funding Your Wallet

You have two main options:

### Option A: Caleb & Brown (UK, recommended)

Caleb & Brown is an OTC broker. Advantages: better rates on larger orders, no slippage, regulated.

1. Open an account at calebandbrown.com
2. Complete identity verification (KYC)
3. Place an order for TAO — give them your coldkey address for delivery
4. They send TAO directly to your wallet within 1-2 business days

### Option B: Coinbase

1. Create a Coinbase account and complete verification
2. Buy TAO directly on the platform
3. Go to "Send" — enter your Bittensor coldkey address
4. Send to your wallet (allow 30 minutes for the transaction to confirm)

### Verify Your Balance

Once the TAO arrives:

```bash
btcli wallet balance --wallet-name tao_main
```

You'll see your TAO balance. **Do not proceed to deployment until you can see the correct balance here.**

---

## PART 6: Building the Deployment Script With Claude Code

Instead of manually running commands for each subnet one at a time, we're going to build a script that does the entire deployment in one go.

```bash
mkdir -p ~/Desktop/TAO_WALLET
cd ~/Desktop/TAO_WALLET
claude
```

**Now paste this prompt into Claude Code:**

---

> **PROMPT — Build the deployment script:**
>
> I want to build a Python script called `tao_deploy.py` that stakes TAO across Bittensor subnets using btcli 9.x.
>
> **My setup:**
> - Wallet name: tao_main
> - Load sensitive values from a .env file in the same directory using python-dotenv
>
> **Positions to deploy to (name, netuid, validator hotkey, percentage):**
> - Root/TAO.com, netuid 0, hotkey 5HK5tp6t2S59DywmHRWPBVJeJ86T61KjurYqeooqj8sREpeN, 50%
> - Chutes, netuid 64, hotkey 5Dt7HZ7Zpw4DppPxFM7Ke3Cm7sDAWhsZXmM5ZAmE7dSVJbcQ, 16.5%
> - Ridges, netuid 62, hotkey 5Djyacas3eWLPhCKsS3neNSJonzfxJmD3gcrMTFDc4eHsn62, 11%
> - Targon, netuid 4, hotkey 5Hp18g9P8hLGKp9W3ZDr4bvJwba6b6bY3P2u3VdYf8yMR8FM, 9.5%
> - Hippius, netuid 75, hotkey 5G1Qj93Fy22grpiGKq6BEvqqmS2HVRs3jaEdMhq9absQzs6g, 7%
> - Nova, netuid 68, hotkey 5F1tQr8K2VfBr2pG5MpAQf62n5xSAsjuCZheQUy82csaPavg, 3.5%
> - Ko/Precog, netuid 55, hotkey 5CzSYnS88EpVv7Kve7U1VCYKjCbtKpxZNHMacAy3BkfCsn55, 2.5%
>
> **Requirements:**
> 1. Accept `--amount` (TAO to deploy) and `--wallet` (wallet name) as CLI arguments
> 2. Verify that the wallet balance is sufficient for the requested amount before doing anything — exit with a clear error if not
> 3. Show a full dry-run summary first — exactly what will be staked where, in TAO and approximate GBP at current price
> 4. Ask the user to type "CONFIRM" (not just press Enter) before executing anything
> 5. Use btcli 9.x syntax: `btcli stake add --netuid X --wallet-name NAME --include-hotkeys HOTKEY` — **do NOT use the -y flag**; present each transaction to the user before it runs
> 6. Run each transaction in sequence, wait for on-chain confirmation before the next
> 7. 300 second timeout per transaction — log clearly if a transaction times out so the user can check which subnets were funded
> 8. Keep it simple — no classes needed
> 9. Load all config from .env using python-dotenv

---

> ⚠️ **Important — read before running:**
> The dry-run preview will show you exactly where each TAO is going. Read it carefully. Verify each netuid and hotkey against [taostats.io](https://taostats.io) before confirming. The script will not use the `-y` flag — each transaction will pause for your confirmation. If a transaction fails or times out, check taostats.io for your wallet address to see which positions were successfully staked.

Claude Code will build the complete script. Test with a dry run first:

```bash
python3 tao_deploy.py --amount 1 --wallet tao_main
```

Review the output carefully. When you're ready to deploy:

```bash
python3 tao_deploy.py --amount 46 --wallet tao_main
```

(Replace 46 with however much TAO is in your wallet.)

---

## PART 7: Building Your Monitoring System With Claude Code

> **Note on the alpha token value formula:** Alpha tokens are priced against TAO via a subnet-specific bonding curve — they do not trade 1:1 with TAO. The formula `value_gbp = alpha_tokens × alpha_price_in_tao × tao_gbp` gives an approximation, but actual GBP value depends on current liquidity and bonding curve state. Treat dashboard GBP values as directional indicators, not precise mark-to-market figures.

> **Note on dashboard data:** The monitor script posts your position data (TAO price, GBP values, position sizes) to your dashboard endpoint. If you are using a shared or third-party dashboard, be aware that this data includes coldkey-linked financial information. Only post to a dashboard you control.

> **PROMPT — Build the monitor:**
>
> Build a Python script called `tao_monitor.py` that runs every hour and tracks my Bittensor positions.
>
> **What it should do:**
> 1. Load config from .env using python-dotenv
> 2. Fetch TAO/GBP price from the CoinGecko API using the COINGECKO_API_KEY from .env. Include retry logic — if the request fails, wait 30 seconds and try once more before giving up
> 3. Connect to Bittensor network using AsyncSubtensor (import bittensor at module level, not inside async functions)
> 4. For each position, call `get_stake_for_coldkey_and_hotkey(coldkey, validator_hotkey)` to get token amounts
> 5. For alpha subnets (not root), call `get_subnet_price(netuid)` to get the alpha/TAO price
> 6. Calculate approximate GBP value: alpha_tokens × alpha_price_tao × tao_gbp (note in comments that this is an approximation based on bonding curve pricing)
> 7. POST a snapshot to DASHBOARD_URL/api/tao-snapshot
> 8. Log all errors clearly — do not fail silently
> 9. Rotate log files: keep a maximum of 7 days of logs, delete older entries automatically
>
> **Config (load from .env):**
> - COLDKEY_ADDRESS, COST_BASIS_GBP, DASHBOARD_URL, COINGECKO_API_KEY
>
> **Positions:** [same 7 positions as above]
>
> **POST payload format:**
> ```json
> {
>   "taoPrice": 214.50,
>   "totalValueGbp": 12500.00,
>   "costBasisGbp": 9805,
>   "pnlGbp": 2695.00,
>   "positions": [
>     { "netuid": 0, "name": "Root", "type": "root", "alphaTokens": 23.15, "priceTao": 1.0, "taoValue": 23.15, "valueGbp": 4966.07 }
>   ]
> }
> ```

---

### What Is a Cron Job?

A cron job is a scheduled task. We're going to set one up that runs your monitor script automatically every hour, every day, without you having to do anything. PM2 handles this.

### A Note on Keeping Your Laptop Awake (macOS only)

For background processes to work, your laptop needs to be on. On Mac, `caffeinate` prevents sleep:

```bash
caffeinate -i &
```

> **macOS only** — this command does not exist on Windows or Linux. On Linux, use `systemd` to manage background services instead of PM2 cron. On Windows, use Task Scheduler.

Alternatively, go to **System Settings → Battery → Options** and enable "Prevent automatic sleeping when display is off."

---

## PART 8: Setting Up the Background Processes

### Create the Monitor Schedule

Create a file called `tao_monitor_ecosystem.config.cjs` in your TAO_WALLET folder:

```javascript
module.exports = {
  apps: [
    {
      name: "tao-monitor",
      script: "/Users/YOURUSERNAME/Desktop/TAO_WALLET/tao_monitor.py",
      interpreter: "python3",
      cron_restart: "0 * * * *",   // runs at the top of every hour
      autorestart: false,
      watch: false,
      out_file: "/Users/YOURUSERNAME/Desktop/TAO_WALLET/tao_monitor.log",
      error_file: "/Users/YOURUSERNAME/Desktop/TAO_WALLET/tao_monitor_err.log",
    },
  ],
};
```

Replace `YOURUSERNAME` with your Mac username (run `whoami` in terminal to find it).

Start it:

```bash
pm2 start tao_monitor_ecosystem.config.cjs
pm2 save
```

---

## PART 9: Building Your Alert System With Claude Code

### Set Up Telegram (5 minutes)

1. Open Telegram on your phone
2. Search for `@BotFather`
3. Send the message: `/newbot`
4. Give your bot a name (e.g. "TAO Watcher")
5. Copy the **bot token** BotFather gives you — it looks like `1234567890:AAABBB...`
6. Search for `@userinfobot` — message it to get your **personal chat ID**
7. Send your new bot one message first (type anything) so it can reach you

Add both to your `.env` file.

### Build the Alert Script

> **PROMPT — Build the alert system:**
>
> Build a Python script called `tao_alerts.py` that runs persistently in the background and manages two alert systems. Load all config from .env using python-dotenv.
>
> **1. Hourly price checker:**
> - Fetch TAO price in USD and GBP from CoinGecko using COINGECKO_API_KEY. If the request fails, send a Telegram alert saying "TAO price check failed — alerts may be unreliable" and retry next cycle. Do not fail silently.
> - Upside alerts — fire once each, never repeat: TAO hits $500 / $3,000 / $10,000 / $30,000
> - Portfolio multiplier alerts — fire once each: 2x / 5x / 10x / 25x of cost basis
> - Drawdown alert: if portfolio value drops more than 30% from its recorded peak, fire a Telegram alert ("⚠️ Portfolio down 30% from peak — consider reviewing your position")
> - Alpha spike alert: if any alpha token price rises >20% since the last check, send alert
> - Deploy window alert: if TAO drops to $240 or below, send alert with deploy instructions (fire once)
> - 14-day deploy reminder: if 14 days pass since deployment with no dip trigger, send a reminder — but include current market context (current price, 30-day price change if available) so the user can make an informed decision rather than deploying automatically
>
> **2. Twitter/X watcher (every 15 minutes):**
> - Fetch RSS feeds from nitter.poast.org/{account}/rss for: const_anto, markjeffrey, bittensor_, tao_dot_com
> - If the RSS fetch fails for any account, send a Telegram alert: "Twitter watcher: feed for @{account} is unavailable — alerts from this account are paused"
> - Check tweet text for keywords: listing, listed, exchange, cex, coinbase, binance, kraken, bybit, okx, kucoin, chutes, ridges, targon, hippius, nova, precog
> - If a new tweet contains a keyword, send Telegram alert with tweet text and link and the note: "⚠️ Verify this directly on X/Twitter — third-party RSS feeds can lag or fail"
> - Track seen tweet IDs to avoid duplicate alerts
>
> **State persistence:**
> - Save all "fired" flags and last-seen tweet IDs to tao_alert_state.json
> - Load the file with error handling: if the JSON is malformed or missing, log the error and start with a clean default state (do not crash)
> - Write atomically: write to a temp file first, then rename, to prevent corruption on sudden shutdown
>
> Use asyncio. Keep it simple.

---

### Start Your Alert System

```bash
pm2 start ~/Desktop/TAO_WALLET/tao_alerts.py --interpreter python3 --name tao-alerts
pm2 save
```

### Survive Reboots

```bash
pm2 startup
```

> ⚠️ **Important:** `pm2 startup` will print a command for you to run. This command typically requires `sudo` (administrator privileges). Read the command before running it — make sure it references pm2 and your username as expected. It should look something like:
> `sudo env PATH=$PATH:/usr/local/bin pm2 startup launchd -u yourusername --hp /Users/yourusername`
>
> If you're unsure what it's asking, paste it into a search engine or ask Claude Code to explain it before running.

After running the printed command:

```bash
pm2 save
```

From that point, your monitor and alert system will restart automatically when your computer starts.

---

## PART 10: The Full Picture — What You've Built

```
YOUR COMPUTER (running 24/7)
│
├── tao-monitor   [runs every hour via cron]
│   └── Bittensor chain → GBP values → Dashboard
│
└── tao-alerts    [runs continuously]
    ├── Price checker (hourly)
    │   ├── Upside alerts: $500 / $3k / $10k / $30k
    │   ├── Drawdown alert: -30% from peak
    │   ├── Portfolio: 2x / 5x / 10x / 25x your investment
    │   ├── Alpha spikes: >20% in 1 hour
    │   └── Deploy window: dip to $240 OR 14-day reminder (with context)
    │
    └── Twitter watcher (every 15 min)
        └── @const_anto, @markjeffrey, @bittensor_, @tao_dot_com
            → keywords → Telegram alert (verify independently)

YOUR DASHBOARD (live, anywhere)
    └── TAO Strategy tab
        ├── Live values per position (approximate)
        ├── Total GBP + PnL
        ├── TAO price
        └── 90-day performance chart

YOUR TELEGRAM
    └── Alerts → your phone, instantly
        (including failure alerts if data sources go down)
```

> **Note on monitoring the monitor:** If PM2 crashes or your machine sleeps, the alert system will stop silently. There is no built-in watchdog for this. Check `pm2 list` periodically to confirm processes are running. A simple workaround: set a recurring phone reminder once a week to run `pm2 list` and verify everything shows "online".

---

## PART 11: Deploying Remaining Capital

The capital you held back should not be deployed at random. Here's the logic:

- **TAO drops to your trigger price** → your Telegram fires. Review the market context in the alert before deciding to deploy.
- **14 days pass with no dip** → your Telegram fires with current price and market context. Deploy only if you're still comfortable with current conditions.

When you decide to deploy:

```bash
python3 ~/Desktop/TAO_WALLET/tao_deploy.py --amount [YOUR_TAO] --wallet tao_main
```

The script will show a full preview and ask you to type CONFIRM before touching anything.

---

## PART 12: Customising for Your Own Strategy

### Choosing Different Subnets

Research subnets at **taostats.io**. Look for:
- Published research papers or technical documentation
- Active development (check the subnet's GitHub)
- Doxxed or publicly known team
- Real-world use cases with evidence of adoption
- Validators with high uptime and significant existing stake

Find the top validator's hotkey on taostats.io and plug it into your `tao_deploy.py` and `tao_monitor.py`. **Verify hotkeys are still active before deploying.**

### Changing Allocation Percentages

Edit the allocation percentages in `tao_deploy.py`. They must add up to 100%.

### Changing Price Targets

Edit the alert thresholds in `tao_alerts.py` to match your own financial goals and risk tolerance.

### Different Capital Size

This works at any size. The percentages are what matter — the absolute amounts follow automatically.

---

## PART 13: Uninstalling / Stopping Everything

If you want to stop the system or start over:

```bash
# Stop all TAO processes
pm2 stop tao-monitor
pm2 stop tao-alerts
pm2 delete tao-monitor
pm2 delete tao-alerts
pm2 save

# Remove scripts and data
rm -rf ~/Desktop/TAO_WALLET

# Remove the wallet (does NOT unstake your TAO — do that via btcli first)
# To unstake: btcli stake remove --netuid X --wallet-name tao_main
# Repeat for each netuid before removing the wallet files
```

> ⚠️ **Unstake before removing the wallet.** Deleting the wallet files while TAO is staked does not unstake it. You need to run `btcli stake remove` for each subnet first, then withdraw to an exchange, before deleting your wallet files. If you lose your seed phrase, you lose access to staked TAO permanently.

---

## The One Thing That Matters

The people who win with Bittensor aren't the ones who understand it best.

They're the ones who act — and who manage risk.

You now understand Bittensor better than most people. You have an automated system. You have an exit strategy. You have monitoring and alerts — including downside alerts.

The only variable left is you.

---

## Quick Reference — Every Command You Need

```bash
# Install everything
pip3 install bittensor requests aiohttp httpx python-dotenv
npm install -g pm2

# Create your wallet
btcli wallet create --wallet-name tao_main

# Check your balance
btcli wallet balance --wallet-name tao_main

# Deploy capital (always review the dry-run preview first)
python3 tao_deploy.py --amount 46 --wallet tao_main

# Start the monitor (hourly, cron-based)
pm2 start tao_monitor_ecosystem.config.cjs

# Start the alert system (persistent, always on)
pm2 start tao_alerts.py --interpreter python3 --name tao-alerts

# Check everything is running
pm2 list

# View recent monitor logs
pm2 logs tao-monitor --lines 50

# View recent alert logs
pm2 logs tao-alerts --lines 50

# Save process list (survive reboots)
pm2 save
pm2 startup   # read the output carefully before running it

# Keep your Mac awake (macOS only)
caffeinate -i &

# Unstake from a subnet (do this before removing wallet)
btcli stake remove --netuid 64 --wallet-name tao_main
```

---

## Resources

| Resource | URL |
|----------|-----|
| Bittensor docs | docs.bittensor.com |
| Subnet explorer | taostats.io |
| TAO.com validator | tao.com |
| Mark Jeffrey on X | @markjeffrey |
| Bittensor Discord | discord.gg/bittensor |
| Claude Code | claude.ai/code |
| Caleb & Brown (UK) | calebandbrown.com |
| CoinGecko API | coingecko.com/en/api |
| **Free auto-setup file** | [link in description] |

---

## Download the Auto-Setup File

In the description below is a link to download `BITTENSOR_AUTOSETUP.md`.

Drop that one file into a folder on your computer, open Claude Code in that folder, and say:

> "Read BITTENSOR_AUTOSETUP.md and build my TAO investment system"

Claude Code will ask you a few questions (your capital amount, your Telegram credentials, your preferences) and then build every script, every config file, and your entire automated system — without you having to type a single prompt manually.

That's the shortcut. Everything in this tutorial, in one file.

---

*This document is a technical tutorial only and does not constitute financial advice. Cryptocurrency investments carry significant risk of loss. Past performance is not indicative of future results. Staking rewards may be taxable — consult a qualified tax professional. Only invest what you can afford to lose entirely.*
