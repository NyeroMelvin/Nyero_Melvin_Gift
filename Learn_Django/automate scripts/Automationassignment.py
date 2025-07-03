import os
import logging
from datetime import datetime, time
import pytz
import certifi
import asyncio

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Setup SSL for httpx used by python-telegram-bot
os.environ['SSL_CERT_FILE'] = certifi.where()

# Logging config
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Config
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8149646252:AAGQH0O9RQI_3qFZajXKnqhL35zTAoCGnpU")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "1954501638")
TIMEZONE = pytz.timezone('Africa/Kampala')

# Messages
MESSAGES = [
    "Monday Motivation: Start strong! 💪 #MondayMotivation",
    "Tuesday Tip: Small steps lead to big results. #TuesdayTip",
    "Wednesday Wisdom: You're halfway there! 🌟 #WednesdayWisdom",
    "Thursday Thought: Progress > perfection. #ThursdayThought",
    "Friday Fun: Weekend is coming! 🎉 #FridayFun",
    "Saturday Vibes: Relax and recharge. ☕ #SaturdayVibes",
    "Sunday Reflection: Plan your week. 📝 #SundayReflection"
]

# Send today's message
async def send_daily_message(context: ContextTypes.DEFAULT_TYPE):
    try:
        day = datetime.now(TIMEZONE).weekday()
        await context.bot.send_message(chat_id=CHAT_ID, text=MESSAGES[day])
        logger.info("Daily message sent.")
    except Exception as e:
        logger.error(f"Failed to send message: {e}")

# /start handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Hi! Your Chat ID is {update.effective_chat.id}.\n"
        "I’ll send daily motivation at 08:00 AM Kampala time.\n"
        "Use /sendnow to send today's message manually."
    )

# /sendnow handler
async def send_now(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Sending today's message...")
    await send_daily_message(context)

# Main bot runner
async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("sendnow", send_now))

    # Schedule the daily message
    app.job_queue.run_daily(
        callback=send_daily_message,
        time=time(8, 0, tzinfo=TIMEZONE)
    )


    logger.info("Bot is running. Daily message scheduled for 08:00 AM Kampala time.")
    await app.run_polling()
if __name__ == '__main__':
    import nest_asyncio
    nest_asyncio.apply()

    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        logger.info("Bot manually stopped.")

