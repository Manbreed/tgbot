import logging
import time


from telegram import Update
from telegram.ext import CallbackContext

def date(update: Update, context: CallbackContext):
    telegram_user = update.effective_user
    bot = context.bot
    chat = update.effective_chat


    logging.info("Команда дата")

    bot.send_message(
        chat_id = chat.id,
        text = "Прямо сейчас " + time.strftime("%H:%M:%S %d.%m.%Y", time.localtime()) + " !"
    )
