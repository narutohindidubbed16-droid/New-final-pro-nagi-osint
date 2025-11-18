# ============================
# 🔧 CONFIG SETTINGS (ENV BASED)
# ============================

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Public channels (username OR channel ID both allowed)
MAIN_CHANNEL = os.getenv("MAIN_CHANNEL")          # e.g. @MyMainChannel
BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL")      # e.g. @MyBackupChannel

# Private channel (no join check)
PRIVATE_CHANNEL = os.getenv("PRIVATE_CHANNEL")    # e.g. https://t.me/+abcde12345

# API URLs
MOBILE_API = os.getenv("MOBILE_API")
GST_API = os.getenv("GST_API")
IFSC_API = os.getenv("IFSC_API")
PINCODE_API = os.getenv("PINCODE_API")
VEHICLE_API = os.getenv("VEHICLE_API")

# Admin
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# Default starting credits
START_CREDITS = int(os.getenv("START_CREDITS", "5"))
