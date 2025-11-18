# ============================
# CONFIG FILE
# ============================

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")

# Required Channels
MAIN_CHANNEL = os.getenv("MAIN_CHANNEL")        # Example: -100123456
BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL")    # Example: -100234567
PRIVATE_CHANNEL = os.getenv("PRIVATE_CHANNEL")  # Example: -100345678

# Admins
ADMINS = list(map(int, os.getenv("ADMINS", "").split()))

# APIs
MOBILE_API = os.getenv("MOBILE_API")
GST_API = os.getenv("GST_API")
IFSC_API = os.getenv("IFSC_API")
PINCODE_API = os.getenv("PINCODE_API")
VEHICLE_API = os.getenv("VEHICLE_API")

# MongoDB
MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = "osintpro"
