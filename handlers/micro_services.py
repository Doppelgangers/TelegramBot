from aiogram import types ,Dispatcher

from scripts.Schedule import Schedule

async def echo(message: types.Message):
    s = Schedule()
    text = s.readText('handlers/ScheduleToDay.json')
    await message.answer(text)


def registerHendlers_commands(dp: Dispatcher):
    dp.register_message_handler(echo)