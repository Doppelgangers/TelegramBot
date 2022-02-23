
from aiogram import Bot , types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

file = open ("configs/token.txt")
telegramToken = file.read()
file.close()

bot = Bot(token=telegramToken)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.delete()
    await message.answer(message.text)



async def on_startup(_):
    print("Good start >_< NOT ERROR")



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)




