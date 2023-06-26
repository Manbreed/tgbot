import os

# Проверка на файл настроек
if not os.path.exists('TelegramService/ENV.py'):
    raise FileNotFoundError('Отсутствует файл с настройками ENV.py')


from TelegramService.ENV import  BOT_TOKEN
from telegram.ext import Updater
from TelegramService.BotSetup import BotSetup

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


# Создание бота, запись апдейтера в переменную
updater = Updater(token=BOT_TOKEN, use_context=True)

# Создание настроек бота, передача обработчика бота
bot_setup = BotSetup(updater.dispatcher)
# Добавляем обработчик команд
bot_setup.add_commands_dispatcher()

# Старт прослушки обновлений
updater.start_polling()
