import requests
from Schedule import Schedule
class ApiBot:

    def __init__(self, token):
        self.TOKEN = token

    def sendMsg(self,id_chat , msg):
        url = 'https://api.telegram.org/bot' + self.TOKEN + '/' + 'sendMessage'
        params = dict(chat_id=id_chat,text=msg)
        web = requests.get(url=url , params=params)
        print('Сообщение отправленно')

bot= ApiBot("1219818658:AAERsK7cI_NPgqPz8naLk1EuS8822FtyudM")
list = Schedule()
ms = list.readText()
mesag = "Расписание на сегодня:" + "\n" + "\n" +ms
print(ms)
bot.sendMsg('761897585' , msg=mesag)

