from aiogram import types ,Dispatcher

from scripts.Schedule import Schedule
from scripts.anime import AnimeList

async def echo(message: types.Message):

    if message.text != "anime":
        s = Schedule()
        text = s.readText('data/schedule/ScheduleToDay.json')
    else:
        ani = AnimeList()
        text = 'Сегодня выходят: \n' + ani.getAnime()
    await message.answer(text)


def registerHendlers_commands(dp: Dispatcher):
    dp.register_message_handler(echo)