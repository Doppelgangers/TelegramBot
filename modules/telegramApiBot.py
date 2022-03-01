import requests


class ApiBot:

    def __init__(self, token):
        self.TOKEN = token

    def sendMsg(self, id_chat, msg):
        url = 'https://api.telegram.org/bot' + self.TOKEN + '/' + 'sendMessage'
        params = dict(chat_id=id_chat, text=msg)
        ms = requests.get(url=url, params=params)
        return True
