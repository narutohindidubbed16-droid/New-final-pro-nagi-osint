# ============================================
# 📌 handlers.py
# All Bot Logic & API Responses
# ============================================

import aiohttp
from datetime import datetime
from telegram import Update
from telegram.ext import ContextTypes

from config import (
    BOT_USERNAME,
    MAIN_CHANNEL,
    BACKUP_CHANNEL,
    PRIVATE_CHANNEL,
    MOBILE_API,
    GST_API,
    IFSC_API,
    PINCODE_API,
    RC_API,
    IMEI_API
)

from keyboards import (
    join_channels_kb,
    main_menu_kb,
    lookup_options_kb,
    ask_input_kb,
    quick_back_kb
)

from database import (
    create_user,
    get_user_credits,
    decrease_credit,
    add_referral
)


# -------------------------------------------------
# CHECK USER JOINED 3 CHANNELS
# -------------------------------------------------
async def is_joined_all(bot, user_id):
    try:
        m1 = await bot.get_chat_member(MAIN_CHANNEL, user_id)
        m2 = await bot.get_chat_member(BACKUP_CHANNEL, user_id)
        m3 = await bot.get_chat_member(PRIVATE_CHANNEL, user_id)

        return (
            m1.status in ("member", "administrator", "creator") and
            m2.status in ("member", "administrator", "creator") and
            m3.status in ("member", "administrator", "creator")
        )
    except:
        return False


# -------------------------------------------------
# /start COMMAND
# -------------------------------------------------
async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    args = ctx.args

    # -------------- REFERRAL ----------------
    ref = None
    if args and args[0].isdigit():
        ref = int(args[0])

    created = create_user(user.id, user.username, user.first_name)

    if created and ref and ref != user.id:
        add_referral(ref, user.id)
        try:
            await ctx.bot.send_message(
                chat_id=ref,
                text=f"🎉 *New Referral!* Someone installed using your link.\nYou received +1 Credit 💳*",
                parse_mode="Markdown"
            )
        except:
            pass

    # -------------- CHANNEL CHECK ----------------
    if not await is_joined_all(ctx.bot, user.id):
        await update.message.reply_text(
            "🔐 *Please join all required channels to unlock the bot:*",
            reply_markup=join_channels_kb(),
            parse_mode="Markdown"
        )
        return

    # -------------- WELCOME ----------------
    await update.message.reply_text(
        f"👋 Welcome to **Nagi OSINT PRO**\nSelect any tool below ⬇️",
        reply_markup=main_menu_kb(),
        parse_mode="Markdown"
    )


# -------------------------------------------------
# VERIFY JOIN BUTTON
# -------------------------------------------------
async def verify_join(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()

    if await is_joined_all(ctx.bot, q.from_user.id):
        await q.message.reply_text(
            "✅ Verified! Access Unlocked.",
            reply_markup=main_menu_kb(),
            parse_mode="Markdown"
        )
    else:
        await q.message.reply_text(
            "❌ Please join all channels first.",
            reply_markup=join_channels_kb()
        )


# -------------------------------------------------
# BUTTON HANDLER
# -------------------------------------------------
async def buttons(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    data = q.data
    await q.answer()

    if data == "lookup_options":
        await q.message.reply_text("🔍 Select Lookup Type:", reply_markup=lookup_options_kb())

    elif data == "help_guide":
        await q.message.reply_text(
            "📘 *HELP GUIDE*\n\nJust click any tool and enter input.\nBot auto fetches LIVE data.",
            reply_markup=quick_back_kb(),
            parse_mode="Markdown"
        )

    elif data == "support":
        await q.message.reply_text(
            "🛠 Support: @AbdulBotz",
            reply_markup=quick_back_kb(),
            parse_mode="Markdown"
        )

    elif data == "quick_search":
        await q.message.reply_text(
            "⚡ Quick Search lets you instantly lookup Mobile, RC, Pincode, IMEI & GST in seconds!",
            reply_markup=quick_back_kb(),
            parse_mode="Markdown"
        )

    # -------- SELECT LOOKUP TYPE ----------
    lookup_modes = {
        "mobile_lookup": "📱 Send Mobile Number:",
        "gst_lookup": "🏢 Send GST Number:",
        "ifsc_lookup": "🏦 Send IFSC Code:",
        "pincode_lookup": "📮 Send Pincode:",
        "vehicle_lookup": "🚗 Send RC Number:",
        "imei_lookup": "🧾 Send IMEI Number:"
    }

    if data in lookup_modes:
        ctx.user_data["mode"] = data
        await q.message.reply_text(
            lookup_modes[data],
            reply_markup=ask_input_kb(),
            parse_mode="Markdown"
        )
        return

    if data == "back_home":
        await q.message.reply_text("🏠 Main Menu:", reply_markup=main_menu_kb())


# -------------------------------------------------
# PROCESS USER MESSAGE
# -------------------------------------------------
async def process_text(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    msg = update.message.text.strip()

    # JOIN CHECK
    if not await is_joined_all(ctx.bot, user.id):
        await update.message.reply_text(
            "🔐 Join all channels first.",
            reply_markup=join_channels_kb()
        )
        return

    if "mode" not in ctx.user_data:
        return

    mode = ctx.user_data["mode"]

    # --------- CREDIT CHECK ----------
    credits = get_user_credits(user.id)
    if credits <= 0:
        await update.message.reply_text(
            "❌ *No credits left!*\nUse /start → Refer & Earn",
            parse_mode="Markdown"
        )
        return

    decrease_credit(user.id)

    await update.message.reply_text("⏳ Fetching data…")

    # --------- API MAPPING ----------
    api_map = {
        "mobile_lookup": MOBILE_API + msg,
        "gst_lookup": GST_API + msg,
        "ifsc_lookup": IFSC_API + msg,
        "pincode_lookup": PINCODE_API + msg,
        "vehicle_lookup": RC_API + msg,
        "imei_lookup": IMEI_API + msg
    }

    url = api_map.get(mode)

    # --------- CALL API ----------
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                data = await r.json()
    except:
        await update.message.reply_text("⚠️ API Error. Try again.")
        return

    # ---------- CLEAN OUTPUT ----------
    formatted = f"📄 *OSINT Result*\n\n```\n{data}\n```"

    await update.message.reply_text(
        formatted,
        parse_mode="Markdown"
    )
