# Ставим лайки на deviantart
# Стимулируем посещение своего профиля.

import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument(r"user-data-dir=C:\Users\moonz\AppData\Local\Google\Chrome")
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=options)



def coments():  # Клик на звёзжочку

    try:
        for i in range(1, 10):
            # В начале каждого цикла будем переходить на страницу что бы получить Свежиую выдачу.
            driver.get("https://www.deviantart.com/newest/")
            time.sleep(2)
            cliking = driver.find_elements_by_xpath("//span[@class='saved-faved-corner']")
            for i in cliking:
                try:
                    # Сон это обязательная часть работы скрипта, его нельзя торогать.
                    time.sleep(2)
                    i.click()
                    time.sleep(2)
                except:
                    continue
        time.sleep(10)  # Ждем загрузки новых работ.
    except:
        print('Ошибка')
    finally:
        driver.close()
        time.sleep(3)
        driver.quit()
        time.sleep(2)

coments()