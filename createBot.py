from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os

file = open ("configs/token.txt")
telegramToken = file.read()
file.close()

bot = Bot(token=telegramToken)
dp = Dispatcher(bot)
