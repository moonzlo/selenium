import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\chromeDriver")
driver = webdriver.Chrome(executable_path="C:\\chromeDriver\chromedriver.exe", chrome_options=options)
driver.get("https://nnm-club.me/forum/portal.php?c=10")


def coments():

    for i in range(1, 17):
        time.sleep(1)
        print('Подождали')
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)"
                                           u"='Продолжительность'])[{}]/following::img[1]".format(str(i))).click()

        time.sleep(1)  # Пришлось использовать из-за того что кнопка спасибо не успевала прогрузиться.
        try:
            senks = driver.find_element_by_xpath(u"//img[@alt='Спасибо']")
            senks.click()  # проверяем не нажата ли кнопка Уже
            driver.back()  # Если НЕТ, то нажимаем и возвращаемся назад
        except Exception as errors:
            print('Ошибка', errors)
            driver.back()  # Если Уже нажата, значит всё равно возвращаемся


    driver.find_element_by_link_text(u"След.").click()


def start():
    try:
        for i in range(1, 100):  # Количество запусков
            coments()
    except Exception as error:
        print(error)
    finally:
        driver.close()
        time.sleep(2)
        driver.quit()
        time.sleep(2)


start()
