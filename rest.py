from selenium import webdriver
import time
def main():
    dr = webdriver.Chrome("chromedriver.exe")
    dr.get('https://lms.synergy.ru/')
    time.sleep(5)
    name  = dr.find_element_by_id("popupUsername")
    name.clear()
    name.send_keys("6666genocide666@mail.ru")

    password = dr.find_element_by_id('popupPassword')
    password.clear()
    password.send_keys("AGNO3Amiak")

    btnAut = dr.find_element_by_id('popupLoginBtn').click()
    time.sleep(5)

    dr.get('https://lms.synergy.ru/schedule/academ')

    htmls = dr.page_source
    print(htmls)
    time.sleep(10)





main()