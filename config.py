# ==========================================
# ⚙️ config.py — Nagi OSINT PRO
# ==========================================

import os

# ------------------------------------------
# BOT CREDENTIALS
# ------------------------------------------
BOT_TOKEN = os.getenv("BOT_TOKEN")              # your bot token
BOT_USERNAME = os.getenv("BOT_USERNAME")        # example: NaGIOsintProBot

# ------------------------------------------
# CHANNELS
# ------------------------------------------
MAIN_CHANNEL = os.getenv("MAIN_CHANNEL")        # @YourMainChannel
BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL")    # @YourBackupChannel
PRIVATE_CHANNEL = os.getenv("PRIVATE_CHANNEL")  # @YourPrivateChannel (NO JOIN CHECK)

# ------------------------------------------
# REFERRAL + CREDITS
# ------------------------------------------
START_CREDITS = int(os.getenv("START_CREDITS", 5))

# ------------------------------------------
# DATABASE (MongoDB)
# ------------------------------------------
MONGO_URI = os.getenv("MONGO_URI")

# ------------------------------------------
# API ENDPOINTS (LIVE WORKING)
# ------------------------------------------
MOBILE_API  = os.getenv("MOBILE_API",  "https://ph-ng-pi.vercel.app/?number=")
PINCODE_API = os.getenv("PINCODE_API", "https://pincode-ng.vercel.app/lookup?pincode=")
RC_API      = os.getenv("RC_API",      "https://vvvin-ng.vercel.app/lookup?rc=")
IMEI_API    = os.getenv("IMEI_API",    "https://ng-imei-info.vercel.app/?imei_num=")

# Future Tools (Not available)
GST_API = ""
IFSC_API = ""

# ------------------------------------------
# COMING SOON LIST (UI MENU)
# ------------------------------------------
COMING_SOON_LIST = [
    "Aadhaar OSINT",
    "PAN OSINT",
    "Passport Lookup",
    "Email OSINT",
    "Voter ID Details",
]

# ------------------------------------------
# OWNER / SUPPORT
# ------------------------------------------
OWNER_USER = os.getenv("OWNER_USER", "@AbdulBotz")
SUPPORT_LINK = "https://t.me/" + OWNER_USER.replace("@", "")

# ------------------------------------------
# UI TEXTS
# ------------------------------------------
WELCOME_TEXT = """
✨ *Welcome to Nagi OSINT PRO* ✨

⚡ Advanced Multi-Search  
🔍 Mobile • IMEI • Vehicle • Pincode  
🎁 Earn credits using referral  
"""

ERROR_TEXT = "⚠️ Something went wrong. Please try again later."
