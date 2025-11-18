# ===============================
# 📌 main.py – Nagi OSINT PRO
# ===============================

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
# 🚀 RUN BOT (Async Safe)
# ---------------------------------------------------
async def run_bot():
    print("🚀 Starting Nagi OSINT PRO...")

    # Build App (LATEST Stable Pattern)
    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .build()
    )

    # ---------------- Commands ----------------
    app.add_handler(CommandHandler("start", start))

    # ---------------- Buttons ----------------
    app.add_handler(CallbackQueryHandler(verify_join, pattern="verify_join"))
    app.add_handler(CallbackQueryHandler(buttons))

    # ---------------- Text Input (Lookup) ----------------
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_text))

    print("✅ Bot is LIVE & Running…")
    await app.run_polling()


# ---------------------------------------------------
# ENTRY POINT (No Loop Errors on Render)
# ---------------------------------------------------
if __name__ == "__main__":
    try:
        asyncio.run(run_bot())
    except RuntimeError:
        # Fix for environments where event loop already running
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run_bot())
