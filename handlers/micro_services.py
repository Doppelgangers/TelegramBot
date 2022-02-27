from aiogram import types, Dispatcher, Bot
from createBot import bot, dp
import logging

from modules.sunergySchedule import SynergySchedule
from modules.anime import AnimeList
from keyBoards import kb_client
from id_user.chek_id_user import Database


db = Database()


async def echo(message: types.Message):

    if message.text == "/start":
        await bot.send_message(message.from_user.id, "Добро пожаловать!", reply_markup=kb_client.mainMenu)
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
            db.set_nickname(message.from_user.id, message.from_user.first_name + ' ' + message.from_user.last_name)

    elif message.text == '🏫 Schedule':
        s = SynergySchedule()
        text = s.readText('data/schedule/ScheduleToDay.json')
    elif message.text == '🎬 Anime':
        ani = AnimeList()
        text = 'Сегодня выходят: \n' + ani.getAnime()
    elif message.text == '➡ Other':
        await bot.send_message(message.from_user.id, 'Побочное меню', reply_markup=kb_client.otherMenu)
    elif message.text == '📜 Main menu':
        await bot.send_message(message.from_user.id, 'Основное меню', reply_markup=kb_client.mainMenu)
    else:
        await bot.send_message(message.from_user.id, "Пока пусто!")
    await message.answer(text)


def registerHendlers_commands(dp: Dispatcher):
    dp.register_message_handler(echo)