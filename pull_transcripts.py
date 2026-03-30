#!/usr/bin/env python3
"""Pull transcripts for all Revenue Search episodes from Siam Kidd's YouTube channel."""

import json
import time
import os
from youtube_transcript_api import (
    YouTubeTranscriptApi,
    NoTranscriptFound,
    TranscriptsDisabled,
)

OUTPUT_DIR = os.path.expanduser("~/Desktop/TAO_WALLET/revenue_search_transcripts")

EPISODES = [
    ("vVZ2daGzUH0", "RS61 - SN46 RESI"),
    ("G8KU0hKdifM", "RS60 - Mark & Siam chat"),
    ("TemN93akCJQ", "RS59 - SN79 MVTRX"),
    ("4QeSSe8mFwI", "RS58 - SN70 Vericore"),
    ("SS4djfGb7O0", "RS57 - SN65 TPN"),
    ("2KYWVld-QeQ", "RS56 - SN6 Numinous"),
    ("Fw2ofCF46qg", "RS55 - Mentat Minds"),
    ("AeCxjFP5-1k", "RS54 - Bittensor Chat"),
    ("J1u9tbImBg0", "RS53 - SN91 Tensorprox"),
    ("E2ty0JzIeFo", "RS52 - Tao.com"),
    ("6W_bRTaEV2Y", "RS51 - SN11 Dippy"),
    ("xpGOYWBUS0k", "RS50 - SN44 Score"),
    ("bFdV6Qs_Za4", "RS49 - SN45 Talisman AI"),
    ("swex1tF73KY", "RS48 - SN71 LeadPoet"),
    ("5qVONT0VpC8", "RS47 - Crucible Labs"),
    ("1MqyeX7Hupw", "RS46 - SN32 Its AI"),
    ("C8gK7OnxEvA", "RS45 - SN113 Taonado"),
    ("UlKf-hhDL8w", "RS44 - SN93 Bitcast"),
    ("xs3OA88ppGA", "RS43 - Mark & Siam chat"),
    ("HEbuj9_GDtY", "RS42 - General TAO Ventures"),
    ("r6wpu9RdJsQ", "RS41 - SN42 Gopher"),
    ("_hlFJEbVoXE", "RS40 - SN85 Vidaio"),
    ("786-XllH5PU", "RS39 - SN46 RESI"),
    ("lbZs1fcf2Ks", "RS38 - SN121 sundae_bar"),
    ("rUHAAYjNPcQ", "RS37 - SN37 Aurelius"),
    ("GFg6iJjNGIA", "RS36 - SN15 BitQuant"),
    ("WRfxeQHObbw", "RS35 - SN10 Swap"),
    ("d5xmii-P9NQ", "RS34 - SN62 Ridges AMA"),
    ("wBcC0D3aohs", "RS33 - SN41 Sportstensor"),
    ("CUxF35A-HJc", "RS32 - Bittensor Guru Keith Singery"),
    ("gzx_-qIUDZ4", "RS31 - SN106 Void AI"),
    ("2PSFeEeUHsc", "RS30 - SN50 Synth"),
    ("Of0YWPYuvtc", "RS29 - SN88 Investing"),
    ("j5Ruftot_ek", "RS28 - SN46 RESI"),
    ("BmhMhqBE5FY", "RS27 - SN75 Hippius"),
    ("oFHJfhBiTMc", "RS26 - SN22 Desearch"),
    ("IPAudpawtsw", "RS25 - James Altucher"),
    ("89knv8Fbg1E", "RS24 - SN18 Zeus"),
    ("hT5u0rYL22o", "RS23 - SN49 Polaris"),
    ("eKrq4P0LdQg", "RS22 - SN123 Mantis"),
    ("3q5l5WU6-ys", "RS21 - Mark Jeffrey dTAO"),
    ("v30aQkBhQGo", "RS20 - SN54 Yanez MIID"),
    ("n6fIcQpQRy4", "RS19 - SN62 Ridges"),
    ("f1FAfhQlYhk", "RS18 - SN93 Bitcast"),
    ("XlUkFg7uakY", "RS17 - SN11 Dippy"),
    ("MBdjXsuSYzw", "RS16 - Halving & Good Bad Subnets"),
    ("owOR9h-Xc18", "RS15 - SN44 Score"),
    ("2Nl7STjDs54", "RS14 - SN4 Targon"),
    ("qnDn_S87ejw", "RS13 - SN61 Red Team"),
    ("VORWOB6z7Ik", "RS12 - SN13 Data Universe"),
    ("qHXSKzdUETg", "RS11 - SN56 Gradients"),
    ("11j3RkOKyKk", "RS10 - SN65 TPN"),
    ("8T9czNqSIeE", "RS09 - SN50 Synth"),
    ("352QEgjD-nY", "RS08 - SN68 Metanova"),
    ("7_AOZjbmp20", "RS07 - SN85 Vidaio"),
    ("qEbA0Bu_F-s", "RS06 - SN64 Chutes"),
    ("7dw8eBgAq2Q", "RS05 - SN16 Hash Tensor"),
    ("pJy9wSY8O1c", "RS00 - Launch"),
    ("-kk3pfBbix4", "RS04 - Subnet Cap Chat"),
    ("aLSc-x5_zd0", "RS03 - SN33 ReadyAI"),
    ("aRNgfWwKsv4", "RS02 - SN34 Bitmind"),
]

os.makedirs(OUTPUT_DIR, exist_ok=True)
success, failed = [], []

for video_id, title in EPISODES:
    safe_title = title.replace("/", "-").replace(":", "")
    out_path = os.path.join(OUTPUT_DIR, f"{safe_title}.txt")

    if os.path.exists(out_path):
        print(f"  [skip] {title} — already exists")
        success.append(title)
        continue

    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=["en", "en-GB", "en-US"])
        text = " ".join(entry.text for entry in transcript)
        with open(out_path, "w") as f:
            f.write(f"# {title}\n# Video ID: {video_id}\n\n{text}")
        print(f"  [ok]   {title} ({len(text):,} chars)")
        success.append(title)
    except (NoTranscriptFound, TranscriptsDisabled):
        print(f"  [skip] {title} — no transcript available")
        failed.append((title, "no transcript"))
    except Exception as e:
        print(f"  [fail] {title} — {e}")
        failed.append((title, str(e)))

    time.sleep(5)

print(f"\n✅ Done: {len(success)} transcripts saved to {OUTPUT_DIR}")
if failed:
    print(f"⚠️  {len(failed)} episodes had no transcript:")
    for t, reason in failed:
        print(f"   - {t}: {reason}")
