import random

import schedule
import datetime
import time
from scripts.Schedule import Schedule
from scripts.postMesage import ApiBot

bot = ApiBot("1219818658:AAERsK7cI_NPgqPz8naLk1EuS8822FtyudM")
sched = Schedule()
def nowSchedule():
    today = datetime.date.today()
    dat = today.strftime('%d.%m.%Y')
    sched.uppdate(dat)

def tomorrowSchedule():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    dat = tomorrow.strftime('%d.%m.%Y')
    sched.uppdate(dat)

def spam():
    tex = sched.readText()
    bot.sendMsg('761897585',  tex)


# schedule.every(60).seconds.do(spam)
schedule.every().day.at("06:00").do(nowSchedule)
schedule.every().day.at("06:30").do(spam)
schedule.every().day.at("20:00").do(tomorrowSchedule)
schedule.every().day.at("20:30").do(spam)
while True:
    schedule.run_pending()
    time.sleep(1)
