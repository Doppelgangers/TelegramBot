import random
import schedule
import datetime
import time
from scripts.Schedule import Schedule
from scripts.postMesage import ApiBot

file = open ("configs/token.txt")
telegramToken = file.read()
file.close()

bot = ApiBot(telegramToken)
sched = Schedule('data/chromedriver.exe')

def nowSchedule():
    today = datetime.date.today()
    dat = today.strftime('%d.%m.%Y')
    sched.uppdate(dat , 'data/schedule/ScheduleToDay.json')

def tomorrowSchedule():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    dat = tomorrow.strftime('%d.%m.%Y')
    dat = '28.02.2022'
    sched.uppdate(dat, 'data/schedule/ScheduleTomorrow.json')

def spamToDay():
    tex = sched.readText('data/schedule/ScheduleToDay.json')
    bot.sendMsg('761897585',  'Расписание на сегодня: \n' + tex)

def spamTomorrow():
    tex = sched.readText('data/schedule/ScheduleTomorrow.json')
    bot.sendMsg('761897585', 'Расписание на завтра: \n' + tex)


schedule.every().day.at("06:00").do(nowSchedule)
schedule.every().day.at("06:30").do(spamToDay)
schedule.every().day.at("20:00").do(tomorrowSchedule)
schedule.every().day.at("20:30").do(spamToDay)
while True:
    schedule.run_pending()
    time.sleep(1)
