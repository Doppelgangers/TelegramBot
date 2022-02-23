from aiogram import types ,Dispatcher
from createBot import dp


async def echo(message: types.Message):
    await message.answer(message.text)


def registerHendlers_commands(dp: Dispatcher):
    dp.register_message_handler(echo)