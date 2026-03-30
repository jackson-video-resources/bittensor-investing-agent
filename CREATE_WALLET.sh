#!/bin/bash
# =============================================================
# STEP 1: Run this to create your Bittensor wallet
# =============================================================
# This will:
#  1. Ask you to set a password (remember it — needed to stake)
#  2. Show you a 12-word mnemonic — WRITE THIS DOWN NOW
#     (it's the only way to recover your wallet)
#  3. Save your coldkey SS58 address to TAO_WALLET.env

echo ""
echo "============================================"
echo "  Creating Bittensor wallet..."
echo "  You will be asked to set a password."
echo "  WRITE DOWN your mnemonic when shown!"
echo "============================================"
echo ""

btcli wallet create --wallet.name tao_main --no_password 2>/dev/null || \
btcli wallet create --wallet.name tao_main

echo ""
echo "============================================"
echo "  Extracting coldkey address..."
echo "============================================"

# Get the SS58 address from the wallet
ADDRESS=$(python3 -c "
import bittensor_wallet as btw
w = btw.Wallet(name='tao_main')
print(w.coldkeypub.ss58_address)
" 2>/dev/null)

if [ -z "$ADDRESS" ]; then
    echo "Could not auto-extract address. Run: btcli wallet overview --wallet.name tao_main"
    echo "Then copy your coldkey SS58 address into TAO_WALLET.env manually."
else
    # Save to env file
    cat > "$(dirname "$0")/TAO_WALLET.env" << EOF
# ============================================================
# TAO WALLET — Lewis Jackson
# Created: $(date)
# ============================================================

# Your Bittensor coldkey address — send TAO here from Binance/MEXC
COLDKEY_ADDRESS=$ADDRESS

# Wallet name (used by btcli and tao_deploy.py)
WALLET_NAME=tao_main
HOTKEY_NAME=default

# Keith Singery validator hotkey — UPDATE THIS from taostats.io
# Go to: https://taostats.io/validators — search "Keith Singery"
KEITH_SINGERY_HOTKEY=REPLACE_WITH_REAL_KEY_FROM_TAOSTATS

# ============================================================
# DEPLOYMENT COMMAND (once TAO is in wallet):
# python3 ~/Desktop/RedDayDCAAlerter/tao_deploy.py --amount 10000 --wallet tao_main --dry-run
# python3 ~/Desktop/RedDayDCAAlerter/tao_deploy.py --amount 10000 --wallet tao_main
# ============================================================
EOF

    echo ""
    echo "✅ Done! Your wallet is ready."
    echo ""
    echo "  COLDKEY ADDRESS (send TAO here):"
    echo "  $ADDRESS"
    echo ""
    echo "  Saved to: $(dirname "$0")/TAO_WALLET.env"
    echo ""
    echo "  NEXT STEPS:"
    echo "  1. Go to taostats.io → Validators → find Keith Singery"
    echo "  2. Copy his SS58 hotkey into TAO_WALLET.env"
    echo "  3. Update tao_deploy.py line 39 with the same key"
    echo "  4. Withdraw £10,000 TAO from Binance/MEXC to your coldkey address above"
fi
