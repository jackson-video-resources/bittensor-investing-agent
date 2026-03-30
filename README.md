# Bittensor Investing Agent

> A fully automated TAO investment system — built with Claude Code in 10 minutes. Monitors your subnet positions every hour, sends Telegram alerts when it's time to act, and runs in the background without you having to do anything.

**As seen in:** [$1,300/Day Automated Bittensor Investing With Claude Code (34 Min Free Masterclass)](https://youtu.be/SHEs8gNh7sQ)

---

## What You're Building

- **Automated portfolio monitor** — checks your TAO and subnet alpha token positions every hour, calculates GBP value and P&L against your cost basis
- **Telegram alerts** — notifies you at price milestones ($500 / $3,000 / $10k / $30k TAO), portfolio multipliers (2x / 5x / 10x), and alpha token spikes (>20% in 1 hour)
- **Live dashboard** — every position visible in real time from any device
- **Runs autonomously** — PM2 keeps everything alive and restarts on reboot

You choose your strategy at setup: follow Lewis's allocation (Mark Jeffrey framework), follow Siam Kidd's allocation (DSV Fund framework), or build your own from scratch.

---

## ▶ Tutorial Video — Start Here

**Full 34-minute walkthrough. Watch this first, then use the setup doc below.**

**[youtu.be/SHEs8gNh7sQ](https://youtu.be/SHEs8gNh7sQ)**

---

## 10-Minute Setup (No Coding Required)

1. Create a folder on your Desktop called `TAO_WALLET`
2. Download **[BITTENSOR_AUTOSETUP.md](./BITTENSOR_AUTOSETUP.md)** into that folder
3. Open Terminal and run:
   ```bash
   cd ~/Desktop/TAO_WALLET
   claude
   ```
4. Say: **"Read BITTENSOR_AUTOSETUP.md and set up my TAO investment system"**

Claude Code reads the setup document and builds everything for you — wallet, monitoring scripts, alerts, dashboard — step by step, asking only the questions it needs.

---

## Prerequisites

| Requirement | How to get it | Cost |
|-------------|--------------|------|
| Claude Code | `npm install -g @anthropic-ai/claude-code` | Free to install |
| Anthropic account | [console.anthropic.com](https://console.anthropic.com) | Pay per use (~$0.50–2 for full setup) |
| Python 3.8+ | [python.org](https://python.org) or `brew install python` | Free |
| Bittensor CLI (`btcli`) | `pip install bittensor` | Free |
| PM2 | `npm install -g pm2` | Free |
| Telegram account | [telegram.org](https://telegram.org) | Free |

---

## Estimated Costs

| Item | Cost |
|------|------|
| Claude Code setup (one-time) | ~$0.50–2.00 |
| Running the monitor | Free (runs locally) |
| Hosting (optional, Railway) | ~$5/month |
| **TAO to invest** | Your choice — the system works at any amount |

---

## Strategy Options

At setup, Claude Code asks which strategy you want to use:

### Option A — Lewis's Allocation (Mark Jeffrey Framework)
Conservative by Bittensor standards. 50% root staking as a stable base, remainder spread across proven subnets.

| Position | Subnet | Allocation |
|----------|--------|-----------|
| Root staking (TAO.com) | SN0 | 50% |
| Chutes | SN64 | 16.5% |
| Ridges | SN62 | 11% |
| Targon | SN4 | 9.5% |
| Hippius | SN75 | 7% |
| Nova | SN68 | 3.5% |
| Ko/Precog | SN55 | 2.5% |

### Option B — Siam Kidd's Allocation (DSV Fund Framework)
More aggressive. Less root staking, higher alpha exposure. Based on publicly disclosed DSV Fund investments.

| Position | Subnet | Allocation |
|----------|--------|-----------|
| Root staking | SN0 | 20% |
| Ridges | SN62 | 25% |
| Synth | SN50 | 20% |
| SCORE | SN44 | 15% |
| Chutes | SN64 | 12% |
| Dippy | SN11 | 8% |

### Option C — Your Own
Tell Claude Code exactly which subnets and what percentages. It builds the system around your choices.

---

## What's in This Repo

| File | What it does |
|------|-------------|
| `BITTENSOR_AUTOSETUP.md` | **The one-shot setup prompt** — paste into Claude Code to build everything |
| `BITTENSOR_MASTERCLASS.md` | Full video script and architecture deep-dive |
| `tao_monitor.py` | Hourly portfolio monitor — checks positions, posts to dashboard |
| `tao_alerts.py` | Persistent alert daemon — Telegram notifications on price/portfolio events |
| `tao_monitor_ecosystem.config.cjs` | PM2 config — keeps both scripts running 24/7 |
| `CREATE_WALLET.sh` | Helper script for wallet creation |
| `.env.example` | Environment variable template |

---

## Running Manually (after setup)

```bash
# Start everything with PM2
pm2 start tao_monitor_ecosystem.config.cjs

# Check it's running
pm2 status

# View live logs
pm2 logs

# Test monitor now (without waiting for cron)
python3 tao_monitor.py

# Test alerts
python3 tao_alerts.py
```

---

## Disclaimer

This system is a **personal portfolio monitoring and alerting tool**. It is not financial advice. Bittensor (TAO) and subnet alpha tokens are highly speculative assets — positions can move significantly in both directions and you could lose your entire investment.

The portfolio performance shown in the tutorial video reflects one individual's results under specific market conditions and is not representative of typical outcomes. Past performance is not indicative of future results.

Before investing, consult a qualified financial adviser. Staking rewards may be taxable in your jurisdiction — consult a tax professional.

---

## License

MIT — do whatever you want with it. A ⭐ on GitHub is appreciated if you found this useful.

---

*Built by [Lewis Jackson](https://youtube.com/@lewiswjackson)*
