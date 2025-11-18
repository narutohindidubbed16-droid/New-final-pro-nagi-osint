# ============================================
# 📌 main.py
# Main Entry – Nagi OSINT PRO Bot
# ============================================

import asyncio
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters
)

from config import BOT_TOKEN
from handlers import (
    start,
    verify_join,
    buttons,
    process_text
)


# ---------------------------------------------------
# 🚀 Start Bot
# ---------------------------------------------------
async def run_bot():
    print("🚀 Starting Nagi OSINT PRO...")

    # Build application
    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .concurrent_updates(True)
        .build()
    )

    # -------------- Commands --------------
    app.add_handler(CommandHandler("start", start))

    # -------------- Callback Buttons --------------
    app.add_handler(CallbackQueryHandler(verify_join, pattern="verify_join"))
    app.add_handler(CallbackQueryHandler(buttons))

    # -------------- Text Handler (Mobile, RC, IMEI, etc) --------------
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_text))

    print("✅ Bot is LIVE & Running…")
    await app.run_polling(close_loop=False)


# ---------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------
if __name__ == "__main__":
    try:
        asyncio.run(run_bot())
    except RuntimeError:
        # For systems that already have a running loop (Replit / Jupyter)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run_bot())
