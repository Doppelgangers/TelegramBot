from selenium import webdriver
from bs4 import BeautifulSoup
import time

def getHtml(data):
    # Создаём браузер в скобках путь к нему
    dr = webdriver.Chrome("chromedriver.exe")
    #Заходим на сайт с формой регистрации
    dr.get('https://lms.synergy.ru/')
    #Ждём пока всё загрузится
    time.sleep(5)
    #===============================================
    # Вводим логин
    name  = dr.find_element_by_id("popupUsername")
    name.clear()
    name.send_keys("6666genocide666@mail.ru")
    # Вводим пороль
    password = dr.find_element_by_id('popupPassword')
    password.clear()
    password.send_keys("AGNO3Amiak")
    #Жмём кнопку входа и ждём загрузки
    btnAut = dr.find_element_by_id('popupLoginBtn').click()
    time.sleep(3)
    #================================================
    #Переходим в отдел расписания
    dr.get('https://lms.synergy.ru/schedule/academ')
    #Выбираем занятия на нужное время
        #дата начала
    data_start = dr.find_element_by_id('dateFrom')
    data_start.clear()
    data_start.send_keys(data)
        # дата окончания
    data_end = dr.find_element_by_id('dateTo')
    data_end.clear()
    data_end.send_keys(data)
        # переход на страницу с нужной датой
    btnGet = dr.find_element_by_id('doSrchBtn').click()
    #Сохраняем html
    html = dr.page_source
    return html


def parser(html):
    soup = BeautifulSoup(html,"lxml")
    page = soup.findAll('td')

    # Удалить мусор
    for i in range(4):
        page.pop(-1)

    day = []




    for i in range(int(len(page)/5)):
        day.append(
            {
            'time'   : page[0].text.replace(" ", "").replace("\n", ""),
            'name'   : page[1].text.strip().replace("\n", ""),
            'audit'  : page[2].text.replace(" ", "").replace("\n", ""),
            'type'   : page[3].text.replace(" ", "").replace("\n", ""),
            'teacher': page[4].text.strip().replace("\n", "")
        }
        )
        for i in range(5):
            page.pop(0)

    return day

def viwe(massive):
    print ("\n" * 100)
    for item in massive:
        print(item['time'] + " | " + item['name'])
    print ("\n" * 10)


if __name__ == '__main__':
    html=getHtml('28.02.2022')
    list = parser(html)
    viwe(list)

