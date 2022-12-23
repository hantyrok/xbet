import configparser

from aiogram import Dispatcher, Bot
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage

config = configparser.ConfigParser()
config.read("settings.ini")
token_bot = config["Bot"]["bot_token"]

bot = Bot(token=token_bot, parse_mode='HTML')

dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)