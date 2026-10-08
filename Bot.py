import os
import random

from telegram import (
    Update,
    InlineQueryResultArticle,
    InputTextMessageContent
)
from telegram.ext import (
    Application,
    InlineQueryHandler,
    ContextTypes
)

TOKEN = os.environ["BOT_TOKEN"]


async def inline_answer(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    question = update.inline_query.query.strip()

    if not question:
        return

    percent = random.randint(1, 100)

    answer = (
        f"❓ Вопрос: {question}\n"
        f"🎲 Вероятность: {percent}%"
    )

    result = InlineQueryResultArticle(
        id=str(random.randint(1, 999999999)),
        title=f"🎲 Вероятность: {percent}%",
        description=question,
        input_message_content=InputTextMessageContent(answer)
    )

    await update.inline_query.answer(
        [result],
        cache_time=0
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(
    InlineQueryHandler(inline_answer)
)

print("Бот запущен!")

app.run_polling()
