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
from handlers import start, verify_join, buttons, process_text


async def run_bot():
    print("🚀 Starting Nagi OSINT PRO...")

    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .build()
    )

    # Commands
    app.add_handler(CommandHandler("start", start))

    # Callback Buttons
    app.add_handler(CallbackQueryHandler(verify_join, pattern="verify_join"))
    app.add_handler(CallbackQueryHandler(buttons))

    # Text input handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_text))

    print("✅ Bot is LIVE & Running…")
    await app.run_polling()


if __name__ == "__main__":
    asyncio.run(run_bot())
