import time
from selenium import webdriver

driver = webdriver.Firefox('D:\profile')
driver.get("https://nnm-club.me/forum/portal.php?c=16&start=1712")


def coments():
    for i in range(1, 17):
        com = driver.find_element_by_xpath(
            u"{}{}{}{}".format("(//img[@alt='Комментарии'])", "[", str(i), "]"))
        com.click()
        time.sleep(2) # Пришлось использовать из-за того что кнопка спасибо не успевала прогрузиться.
        try:
            senks = driver.find_element_by_xpath(u"//img[@alt='Спасибо']")
            senks.click()  # проверяем не нажата ли кнопка Уже
            driver.back()  # Если НЕТ, то нажимаем и возвращаемся назад
        except:
            driver.back()  # Если Уже нажата, значит всё равно возвращаемся

    driver.find_element_by_link_text(u"След.").click()

def start():
    for i in range(1, 100): # Количество запусков
        coments()

start()