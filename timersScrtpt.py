from aiogram.utils import executor
from aiogram import Bot , types
from aiogram.dispatcher import Dispatcher

import schedule
import time

def job():
    print("I'm working...")

schedule.every(1).second.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)

