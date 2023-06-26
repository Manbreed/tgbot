import logging


from telegram import Update
from telegram.ext import CallbackContext


def test(update: Update, context: CallbackContext):
    telegram_user = update.effective_user
    bot = context.bot
    chat = update.effective_chat

    logging.info("Команда тест")

    bot.send_message(
        chat_id = chat.id,
        text = "Привет," + telegram_user.name + "!"
    )
