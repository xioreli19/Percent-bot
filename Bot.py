from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import random
import os

TOKEN = os.environ["BOT_TOKEN"]

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "@XRpercentbot" in text:
        percent = random.randint(1, 100)

        await update.message.reply_text(
            f"🎲 Вероятность: {percent}%"
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, message))

print("Бот запущен!")
app.run_polling()
