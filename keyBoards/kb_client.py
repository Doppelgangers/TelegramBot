from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('📜 Main menu')

# Main Menu
btnAnime = KeyboardButton('🎬 Anime')
btnSchedule = KeyboardButton('🏫 Schedule')
btnOther = KeyboardButton("➡ Other")
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAnime, btnSchedule, btnOther)

# OtherMenu
bthWeather = KeyboardButton('🌨 Weather')
btnWallet = KeyboardButton('💸 Wallet')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(bthWeather, btnWallet, btnMain)