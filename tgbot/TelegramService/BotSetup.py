from telegram.ext import Dispatcher, CommandHandler

from TelegramService.Commands.functions.test import test
from TelegramService.Commands.functions.date import date


class BotSetup:

    def __init__(self, dispatcher: Dispatcher):
        self.dispatcher = dispatcher

    def add_commands_dispatcher(self):
        self.dispatcher.add_handler(CommandHandler("test", test))
        self.dispatcher.add_handler(CommandHandler("date", date))
