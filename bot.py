from aiogram.utils import executor
from createBot import dp

import schedule


async def on_startup(_):
    print("Good start >_< NOT ERROR")

from handlers import micro_services
micro_services.registerHendlers_commands(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)




