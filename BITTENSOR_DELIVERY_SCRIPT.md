# Bittensor Masterclass — Delivery Script
### Format inspired by Riley Brown's long-form tutorial style

---

> **How to use this doc**
> This is your teleprompter. Each section maps to a live screen recording segment.
> `[SLIDE: X]` = switch to that FigJam diagram on screen
> `[SCREEN: X]` = share your screen showing that app or terminal
> `[PROMPT]` = show and walk through the exact Claude Code prompt
> Casual delivery. Short sentences. "Right?" as a verbal check-in. Show everything live.

---

## COLD OPEN (before title card)

We are at one of those rare moments in history where two of the most powerful forces in technology — AI and blockchain — are converging at the same time.

And I am positioned for it. Not just with an investment in TAO and a selection of its most promising subnets. But with a fully automated system built around that investment.

As prices move up, milestones are set. When those milestones are hit — profits are taken and redistributed automatically according to the strategy. When something important happens in the market — a major announcement, a listing, a spike in one of my subnet positions — I get a notification on my phone. I don't have to be at my computer. I don't have to be watching anything.

The entire strategy is running in the background. On its own.

And the remarkable thing is how I built it. I used Claude Code — Anthropic's AI coding tool. I described what I wanted in plain English. It built the scripts, set up the wallet security, configured the monitoring, wrote the alert system. All of it. With prompts. No coding experience required.

That's what we're doing in this video. I'm going to give you every single prompt. Every step of the process. And by the end of today you're going to walk away with three things.

*[SLIDE: intro card — the 3 promises]*

---

## INTRO

*[SLIDE: intro card — the 3 promises]*

Hello. I'm Lewis. This is the complete Bittensor masterclass.

Quick thing before we start — this video assumes you already know what Bittensor is. You know about TAO. You know about the subnets. You're here because you want to invest properly and you want the whole thing automated. That's exactly what we're building.

If you're not there yet — save this video, subscribe to the channel. We've got people coming on very soon who are going to explain the full Bittensor story in depth. Come back to this video when you've done that.

For everyone else — here's where we're going.

By the end of this you are going to have your capital deployed across Bittensor's most promising AI subnets, a fully running automated system on your machine tracking your positions in real time, Twitter monitored for market-moving news, and alerts firing straight to your phone the moment something matters.

We're covering the strategy. The exact prompts you give Claude Code at every single step. The tools. The security. How to buy TAO. How to deploy it. How to keep it all running in the background.

And at the end — I'm giving something away that means you could do this entire thing in under ten minutes. No email. No purchase. No sales pitch. I just want people to make an obscene amount of money this year.

Let me tell you who I am quickly and then we're straight into it.

---

## WHO AM I (45 seconds)

I run the 10x Challenge — my goal is to turn £50,000 into £500,000 and I document every trade, every decision, in public. Link in the description. You can see my live TAO positions on the dashboard right now.

TAO is my highest conviction position. I've put £20,000 in. £15,000 deployed across seven AI subnets. £5,000 held back deliberately — with an automated system that tells me when to deploy it.

I'm up 28% in 48 hours. The system is working.

Let's build it.

---

## SECTION 1: MY CONVICTION AND THE STRATEGY SOURCE

> *Don't follow along yet. Just listen.*

You already know what Bittensor is. So I'm not going to explain it. What I want to tell you is why I put £20,000 of my own money in — and whose research I used to decide exactly where.

---

You know about dTAO. You know about root staking and alpha tokens. So you already understand the basic split — root staking earns TAO passively regardless of which subnet wins, and alpha tokens are your asymmetric bets on specific subnets.

*[SLIDE: root staking vs alpha tokens]*

The question isn't whether to use both. The question is how much to allocate where. And that decision should be based on research — not guesswork.

---

### Mark Jeffrey

The allocation I'm running is based on the work of Mark Jeffrey — one of the most rigorous researchers in the Bittensor ecosystem. He spent hundreds of hours going through every subnet. The technology, the team, the validator economics, the emission schedules.

I studied his framework and built my system around it. We're trying to get Mark on the podcast — genuinely hard to reach — but we do have an episode coming with Rob Greer, who works closely with him and is equally deep on this. Subscribe so you don't miss that.

The point: don't just copy my allocation. Use this video to build the system, then point it at whatever research you trust most. That's exactly what Claude Code is going to let you do.

---

## SECTION 2: THE STRATEGY

> *Still mainly talking. Show the diagrams. No terminal yet.*

Okay, section two. The actual strategy.

Here's the allocation I'm using.

*[SLIDE: exit strategy — show this while walking through the allocation]*

Fifty percent goes to root staking. This is your anchor. This earns TAO passively and it gives you exposure to the whole network, not just one subnet. I'm staking this with Keith Singery at TAO.com — Rank 5 validator, some of the best uptime in the network.

The remaining fifty percent is split across six alpha subnets. And here's how I think about these:

**Chutes** — SN64. AI inference marketplace. If you've used a GPU API, this is that. But decentralised. Sixteen and a half percent.

**Ridges** — SN62. Financial prediction. Eleven percent.

**Targon** — SN4. Text generation. Nine and a half percent.

**Hippius** — SN75. Decentralised cloud compute. Seven percent.

**Nova** — SN68. Data pipelines. Three and a half percent.

**Ko/Precog** — SN55. Market prediction. Two and a half percent.

You only need one of these to win big. That's the whole thesis. You're betting on a basket. And the root staking means you still earn regardless.

---

### The Exit Plan

I want to be very clear about this because I think most people get this wrong.

*[SLIDE: exit strategy]*

This is not a trade. This is a multi-year hold. But you need a plan that you make in advance — when you're calm — so that your emotions don't make the decision for you when things get wild.

My plan:

TAO hits $500 — I take 25% off the root staking. I've recovered my cost basis. The rest stays.

TAO hits $3,000 — I take 25% off everything. I've locked in life-changing money. The rest stays.

TAO hits $10,000 — I take another 25% off. Reassess the remainder.

TAO hits $30,000? I hold everything. The full Bitcoin thesis is playing out. At $100,000 per TAO, a single token is worth about £80,000. You do not want to be the person who sold at five hundred.

Twenty-five percent at each milestone. Never more. Right?

---

## HALF TIME

Okay. I'm going to call half time here.

We've covered a lot. Let me recap before we get into the actual build.

Section one — the case for TAO. We talked about why this is the Bitcoin moment for AI. dTAO, root staking versus alpha tokens, Mark Jeffrey's research.

Section two — the strategy. Seven positions. Fifty percent root, fifty percent alpha across six subnets. Exit plan at $500, $3k, $10k, $30k — 25% off at each milestone.

Now we're going to actually build this. And this is where it gets fun.

In section three — I'm going to show you every single Claude Code prompt that built this system. Live. On screen. You're going to follow along.

And at the end of section four — I'm revealing the file that automates all of it.

Let's go.

---

## SECTION 3: BUILDING THE SYSTEM

> *Follow along from here. Terminal and Claude Code on screen.*

Okay. From this point forward, follow along on your own machine if you can.

---

### Step 1: Install Bittensor

```bash
pip3 install bittensor
```

This gives you the `btcli` tool — the command line interface for Bittensor. Think of it like your bank's online portal, except it talks directly to the blockchain.

Verify it worked:

```bash
btcli --version
```

---

### Step 3: Create Your Wallet

This is important. Really important.

```bash
btcli wallet create --wallet-name tao_main
```

Your wallet has a **coldkey** — your main address, where your TAO lives — and a 12-word **seed phrase**. The seed phrase is the master key to everything.

Write it down with a pen and paper. Right now. Not in Notes. Not in a screenshot. On paper. In a drawer. Treat it like £50,000 in cash — because that's what it could become.

---

### The .env File

*[SLIDE: .env concept]*

When Claude Code builds your scripts, it creates something called an `.env` file. Here's what that is in plain English.

It's just a text file. It stores sensitive information your scripts need to run — your wallet address, your Telegram token, your settings. Your scripts read from it automatically.

Think of it like a private notebook your computer can read from but no one else can.

Rules:
- Never share it
- Never upload it to Google Drive or GitHub
- Back it up to a USB drive

I spoke to Patrick Delaney — CEO of Amply — on the podcast about exactly this. His whole company is built around securing seed phrases and private keys when you're building systems like this. Worth knowing about. Link in the description.

For now: your `.env` on your local machine is enough to get started. Just treat it like cash.

---

### Step 4: Buy TAO

Two options. UK: **Caleb & Brown**. OTC broker, regulated, best rates on larger orders. 1-2 days for delivery.

Everywhere else: **Coinbase**. Buy TAO, hit send, paste your coldkey address. 30 minutes to arrive.

Once it's there:

```bash
btcli wallet balance --wallet-name tao_main
```

You'll see your TAO.

---

### Step 5: Build the Deployment Script

Okay. This is where Claude Code comes in. We're going to build the script that deploys capital across all seven positions in one go.

*[SCREEN: Claude Code in terminal]*

Open your terminal. Navigate to your TAO folder:

```bash
mkdir -p ~/Desktop/TAO_WALLET
cd ~/Desktop/TAO_WALLET
claude
```

Now paste this prompt. This is the exact one I used.

*[PROMPT — show full prompt on screen, read it out]*

```
I want to build a Python script called tao_deploy.py that automatically
stakes TAO across Bittensor subnets using btcli 9.x.

Wallet name: tao_main. Load sensitive values from a .env file.

Positions to deploy to (name, netuid, validator hotkey, percentage):
- Root/TAO.com, netuid 0, hotkey 5HK5tp6t2S59DywmHRWPBVJeJ86T61KjurYqeooqj8sREpeN, 50%
- Chutes, netuid 64, hotkey 5Dt7HZ7Zpw4DppPxFM7Ke3Cm7sDAWhsZXmM5ZAmE7dSVJbcQ, 16.5%
- Ridges, netuid 62, hotkey 5Djyacas3eWLPhCKsS3neNSJonzfxJmD3gcrMTFDc4eHsn62, 11%
- Targon, netuid 4, hotkey 5Hp18g9P8hLGKp9W3ZDr4bvJwba6b6bY3P2u3VdYf8yMR8FM, 9.5%
- Hippius, netuid 75, hotkey 5G1Qj93Fy22grpiGKq6BEvqqmS2HVRs3jaEdMhq9absQzs6g, 7%
- Nova, netuid 68, hotkey 5F1tQr8K2VfBr2pG5MpAQf62n5xSAsjuCZheQUy82csaPavg, 3.5%
- Ko/Precog, netuid 55, hotkey 5CzSYnS88EpVv7Kve7U1VCYKjCbtKpxZNHMacAy3BkfCsn55, 2.5%

Requirements:
1. Accept --amount and --wallet as CLI arguments
2. Show a dry-run summary first
3. Ask for confirmation before executing
4. Use btcli 9.x syntax: btcli stake add --netuid X --wallet-name NAME
   --include-hotkeys HOTKEY -y
5. Run each transaction in sequence. Wait for confirmation. 300s timeout.
6. Log every step clearly.
```

*Walk through what Claude Code generates. Show the file it creates.*

When it's done — dry run first:

```bash
python3 tao_deploy.py --amount 5 --wallet tao_main
```

See exactly what it would do. Then when you're ready, run it for real. Each transaction takes 1-3 minutes. Full deployment is about 15 minutes. Let it run.

---

### Step 6: Build the Monitor

Now we build the script that checks your positions every hour and keeps your data updated.

*[PROMPT — show on screen]*

```
Build a Python script called tao_monitor.py that runs every hour.

Load config from .env — COLDKEY_ADDRESS, COST_BASIS_GBP, DASHBOARD_URL.

What it does:
1. Fetch TAO/GBP price from CoinGecko
2. Connect to Bittensor: AsyncSubtensor(network="finney")
3. For each position: get_stake_for_coldkey_and_hotkey(coldkey, validator_hotkey)
4. For alpha subnets: get_subnet_price(netuid) for price
5. Calculate: value_gbp = tokens × price_tao × tao_gbp
6. POST snapshot to DASHBOARD_URL/api/tao-snapshot
   (or save to /tmp/tao_latest.json if no dashboard)

Same 7 positions as tao_deploy.py.

Critical: import bittensor at module level. Not inside async functions.
That causes the script to hang.
```

---

### Step 7: Build the Alert System

*[SLIDE: alert system]*

This is the unfair advantage. Right?

While other investors are manually checking CoinGecko, your system is doing this for you 24/7. Let me show you what it watches.

*[Point to each alert on the diagram as you describe it]*

TAO price thresholds. Portfolio milestones. Alpha spikes. Twitter. And a deploy window alert — fires when it's a good time to add more capital.

*[PROMPT — show on screen]*

```
Build a Python script called tao_alerts.py that runs persistently.

Load config from .env.

Hourly price checker:
- Fetch TAO USD + GBP from CoinGecko
- Alert on: $500, $3,000, $10,000, $30,000 — fire once each, save to state
- Alert on portfolio multipliers: 2x, 5x, 10x, 25x of COST_BASIS_GBP
- Alert if any alpha token rises >20% since last check
- Alert if TAO drops to DEPLOY_TRIGGER_USD (fire once)
- Alert after 14 days if no dip has come (fire once)

Twitter watcher (every 15 minutes):
- RSS from nitter.poast.org/{account}/rss for:
  const_anto, markjeffrey, bittensor_, tao_dot_com
- Keywords: listing, listed, exchange, cex, coinbase, binance,
  chutes, ridges, targon, hippius, nova, precog
- New tweet + keyword = Telegram alert
- Track seen tweet IDs in state file

All alerts go to Telegram via sendMessage API.
Persist state to tao_alert_state.json.
```

---

### Step 8: Set Up Telegram

Real quick — Telegram setup takes 5 minutes.

*[SCREEN: Telegram on phone]*

Open Telegram. Search @BotFather. Send `/newbot`. Name your bot anything. Copy the token it gives you.

Then search @userinfobot — it tells you your personal chat ID. One message, you get the number.

Add both to your `.env` file. Done. The alert system will now text you directly.

---

### Step 9: Start Everything Running

*[SCREEN: terminal]*

```bash
npm install -g pm2
pm2 start tao_monitor_ecosystem.config.cjs
pm2 start ~/Desktop/TAO_WALLET/tao_alerts.py \
  --interpreter python3 --name tao-alerts
pm2 save
pm2 startup
```

PM2 is a background process manager. Think of it like hiring someone to sit at your computer and run these scripts while you get on with your life. Right?

One more thing — your laptop needs to stay awake for the cron jobs to fire. On Mac:

```bash
caffeinate -i &
```

That tells your Mac to stay on while it's plugged in. Like propping the door open. That's it.

*[Show `pm2 list` output. Both processes online.]*

That's your system running.

---

## SECTION 4: THE 10-MINUTE REVEAL

Okay. You've seen everything I built. You've seen every prompt. You know the strategy, the allocation, the exit plan, the monitoring, the alerts.

Now I'm going to give you the shortcut.

In the description below there's something I've put together that means you can skip every step I just showed you.

Download it. Drop it into a folder on your Desktop. Open Claude Code. Say one sentence:

> *"Read BITTENSOR_AUTOSETUP.md and set up my TAO investment system"*

From there, Claude Code takes over. It asks you whether you want to follow my exact strategy or build your own based on different research. It asks your capital amount, your Telegram details, your preferences. Then it builds every script, every config, your entire automated system — by itself.

Everything I just spent an hour walking you through. Done in ten minutes. Automatically.

I'm not holding anything back. There is no sales pitch. I'm not taking your email. I genuinely believe Bittensor and its subnets are the most important trade of this decade and I want as many people as possible to be positioned for it before the rest of the world catches up.

It's in the description. It's free. It takes ten minutes.

---

## OUTRO

Okay. Let me recap everything we covered.

Section one — the case for TAO. The Bitcoin moment for AI. dTAO, root staking versus alpha tokens.

Section two — the strategy. Mark Jeffrey's allocation. Seven positions. Exit plan at each price milestone.

Section three — the build. Every Claude Code prompt. The deployment script, the monitor, the alert system, Telegram. PM2 running it all in the background.

Section four — the ten-minute file. In the description. Free. No catch.

One last thing. The people who win here aren't the ones who understand it best. They're the ones who act.

You now understand Bittensor better than 99% of the population. You have the system. You have the strategy. You have the exit plan.

The only variable left is you.

See you in the next one.

---

> **Slide cue summary for editing:**
> - SLIDE: intro card → cold open through intro section
> - SLIDE: root vs alpha → explaining the two investment types in Section 1
> - SLIDE: exit strategy → walking through the price milestones in Section 2
> - SLIDE: .env concept → explaining the .env file in Step 3
> - SLIDE: alert system → introducing the alert script in Step 7
> - SCREEN: terminal → all build steps in Section 3
> - SCREEN: Telegram → Step 8
