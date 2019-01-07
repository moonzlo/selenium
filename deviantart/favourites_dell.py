from selenium import webdriver
import time
"""Данная конфигурация реализует базовую настройку с использованием профиля пользователя """

options = webdriver.ChromeOptions()
#options.add_argument('headless')  # Без GUI
options.add_argument(r"user-data-dir=/home/moonz/chrome/profile")
driver = webdriver.Chrome(executable_path="/home/moonz/chrome/chromedriver", chrome_options=options)
# driver.page_source

# Чистим закладки

def start():
    driver.get("https://www.deviantart.com/moonz666/favourites/")

    # Кликаем на первый элпент списка.
    driver.find_element_by_xpath(
        "(.//*[normalize-space(text()) and normalize-space(.)='Search Favourites'])[1]/following::img[1]").click()
    time.sleep(2)  # Ждём загрузку


def clean():

    # Кликаем на кнопку (убрать из закладок)
    time.sleep(1)
    driver.find_element_by_id("gmi-ResourceViewFavouriteButton").click()
    # Переходим на следующую картинку
    time.sleep(1)
    driver.find_element_by_link_text("Next").click()
    time.sleep(1)




try:
    start()
    for i in range(1,500):
        try:
            clean()
        except Exception as error:
            print('Ошибка вышла: ', error)
            start()
            continue


except Exception as er:
    print(er)

finally:
    driver.close()
    time.sleep(2)
    driver.quit()
    time.sleep(2)

