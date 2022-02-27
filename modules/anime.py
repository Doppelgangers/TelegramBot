import requests
from bs4 import BeautifulSoup
class AnimeList:
    def __init__(self):
        pass

    def getAnime(self):
        head= {'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 Mobile Safari/537.36'}
        page=requests.get('https://you-anime.ru/schedule',headers=head)
        soup = BeautifulSoup(page.text, "lxml")
        today=soup.find(class_='date-row')
        nameList = today.findAll(class_= 'field-title')
        dataList = today.findAll(class_='episodes-serial-season')

        list = []
        if len(nameList) == len(dataList):
            for i in range(len(nameList)):
                list.append({
                'name' : nameList[i].text.replace('\n' ,''),
                'info' : dataList[i].text
                })

        answere = ''
        for i in range(len(nameList)):
            answere += list[i]['name'] + "\n" + list[i]['info'] + '\n'+'\n'
        return answere

