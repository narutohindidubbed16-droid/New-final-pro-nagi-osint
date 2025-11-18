# ============================
# 🔧 CONFIG SETTINGS (ENV BASED)
# ============================

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Channel IDs (must be negative integer IDs)
MAIN_CHANNEL = int(os.getenv("MAIN_CHANNEL"))
BACKUP_CHANNEL = int(os.getenv("BACKUP_CHANNEL"))
PRIVATE_CHANNEL = int(os.getenv("PRIVATE_CHANNEL"))

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
