# ==========================================
# 📌 keyboards.py
# Custom Inline Keyboards for OSINT PRO
# ==========================================

from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from config import MAIN_CHANNEL, BACKUP_CHANNEL, PRIVATE_CHANNEL


# -----------------------------
# Channel Join Buttons
# -----------------------------
def join_channels_kb():
    kb = [
        [InlineKeyboardButton("📢 JOIN Main Channel", url=f"https://t.me/{MAIN_CHANNEL.replace('@','')}")],
        [InlineKeyboardButton("📣 JOIN Backup Channel", url=f"https://t.me/{BACKUP_CHANNEL.replace('@','')}")],
        [InlineKeyboardButton("🔐 JOIN Private Channel", url=f"https://t.me/{PRIVATE_CHANNEL.replace('@','')}")],
        [InlineKeyboardButton("✅ I HAVE JOINED ALL CHANNELS", callback_data="verify_join")]
    ]
    return InlineKeyboardMarkup(kb)


# -----------------------------
# Main Menu Keyboard
# -----------------------------
def main_menu_kb():
    kb = [
        [InlineKeyboardButton("🔍 LOOKUP OPTIONS", callback_data="lookup_menu")],
        [
            InlineKeyboardButton("📚 HELP GUIDE", callback_data="help"),
            InlineKeyboardButton("🛠 SUPPORT", callback_data="support")
        ],
        [InlineKeyboardButton("🚀 QUICK SEARCH", callback_data="quick_search")]
    ]
    return InlineKeyboardMarkup(kb)


# -----------------------------
# Lookup Options Keyboard
# -----------------------------
def lookup_menu_kb():
    kb = [
        [
            InlineKeyboardButton("📱 MOBILE LOOKUP", callback_data="mobile_lookup"),
            InlineKeyboardButton("🏢 GST LOOKUP", callback_data="gst_lookup")
        ],
        [
            InlineKeyboardButton("🏦 BANK IFSC", callback_data="ifsc_lookup"),
            InlineKeyboardButton("📮 PINCODE", callback_data="pincode_lookup")
        ],
        [
            InlineKeyboardButton("🚗 VEHICLE LOOKUP", callback_data="vehicle_lookup")
        ],
        [InlineKeyboardButton("🔙 BACK TO MENU", callback_data="back_home")]
    ]
    return InlineKeyboardMarkup(kb)


# -----------------------------
# Quick Search — Try Now + Back
# -----------------------------
def quick_search_kb():
    kb = [
        [InlineKeyboardButton("🔎 TRY NOW", callback_data="quick_try")],
        [InlineKeyboardButton("🔙 BACK", callback_data="back_home")]
    ]
    return InlineKeyboardMarkup(kb)


# -----------------------------
# Back Only
# -----------------------------
def back_kb():
    kb = [[InlineKeyboardButton("🔙 BACK", callback_data="back_home")]]
    return InlineKeyboardMarkup(kb)


# -----------------------------
# Ask Input Keyboard (Cancel)
# -----------------------------
def ask_input_kb():
    kb = [[InlineKeyboardButton("🔙 BACK", callback_data="back_home")]]
    return InlineKeyboardMarkup(kb)
