from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json

class Schedule:
    def __init__(self , patchOfChrome= 'data/chromedriver.exe'):
        self.patchOfChrome = patchOfChrome

    def uppdate(self, date = '25.02.2022' , patchSave = 'data/schedule/ScheduleToDay.json'):
    ### В фунцию передаётся дата в формате dd.mm.yyyy ###
    #   return 'ErrorLoad' происходит если не успел браузер загрузиться или не найден элемент который запланирован
    #   return 'free' выходной
    #   return 'True' программа сохранила расисание
        # Создаём браузер в скобках путь к нему
        dr = webdriver.Chrome(self.patchOfChrome)

        time.sleep(5)
        # Заходим на сайт с формой регистрации
        dr.get('https://lms.synergy.ru/')

        # Ждём пока всё загрузится
        time.sleep(10)
        # ===============================================

        try:
        # Вводим логин
            name = dr.find_element_by_id("popupUsername")
            name.clear()
            name.send_keys("6666genocide666@mail.ru")

            # Вводим пороль
            password = dr.find_element_by_id('popupPassword')
            password.clear()
            password.send_keys("AGNO3Amiak")

            # Жмём кнопку входа и ждём загрузки
            btnAut = dr.find_element_by_id('popupLoginBtn').click()
        except:
            print('ERROR : ErrorLoad 1')
            return 'ErrorLoad'
            # ================================================
        time.sleep(10)

        # Переходим в отдел расписания
        dr.get('https://lms.synergy.ru/schedule/academ')
        # Выбираем занятия на нужное время

        try:
                # дата начала
            data_start = dr.find_element_by_id('dateFrom')
            data_start.clear()
            data_start.send_keys(date)

                # дата окончания
            data_end = dr.find_element_by_id('dateTo')
            data_end.clear()
            data_end.send_keys(date)
                # переход на страницу с нужной датой
            btnGet = dr.find_element_by_id('doSrchBtn').click()
            # ================================================
        except:
            print('ERROR : ErrorLoad 2')
            return 'ErrorLoad'

        # Преобразуем полученный html в обект python
        html = dr.page_source

        #Ищем поля с расписанием
        soup = BeautifulSoup(html, "lxml")

        try:
            page = soup.findAll('td')
        except:
            print('ERROR : Not Found { soup.findAll("td") } ')
            return 'ErrorLoad'

        # Если страница не содержит
        if len(page) == 1:
            print("Выходной")
            with open(patchSave, 'w') as fout:
                json.dump({'msg':'free'}, fout)
            return 'free'

        # Удалить мусор (последнии 4 td содержат не расписание)
        for i in range(4):
            page.pop(-1)

        days = []
        if len(page) % 5 != 0:
            print('Error : Записей не 5 , скорее всего это не расписание или сайт изменился')
            print('Записаей ' + len(page))
            print(page)
            return 'Error'

        # Записываем расписание в список словарей
        for i in range(int(len(page) / 5)):
            days.append(
                {
                    'time': page[0].text.replace(" ", "").replace("\n", ""),
                    'name': page[1].text.strip().replace("\n", ""),
                    'audit': page[2].text.replace(" ", "").replace("\n", ""),
                    'type': page[3].text.replace(" ", "").replace("\n", ""),
                    'teacher': page[4].text.strip().replace("\n", "")
                }
            )
            for i in range(5):
                page.pop(0)

        # Сохраняем в json файл
        with open(patchSave, 'w') as fout:
            json.dump(days, fout)
        print('Save!')
        return True


    def readText(self,path='ScheduleToDay.json'):
        ### Просто считывает сохранённый ранее файл и выдаёт как текст ###
        with open(path, "r") as read_file:
            data = json.load(read_file)
            try:
                if data['msg'] == 'free':
                    return "Выходной"
            except:
                pass
        text = ''
        for i in range(len(data)):
            text += data[i]['time'] + "\n" + data[i]['name'] + "\n" + "\n"
        return text

    def readJSON(self , path='ScheduleToDay.json' ):
        ### Просто считывает сохранённый ранее файл и выдаёт как список словарей ###
        with open(path, "r") as read_file:
            data = json.load(read_file)
        return data

# if __name__ == '__main__':
#     schedule = Schedule()
#     schedule.uppdate('29.02.2022')
#     print(schedule.read())
