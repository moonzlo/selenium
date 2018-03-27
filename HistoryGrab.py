# Собираем историю поисковых запросов с ютуба

import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')  # Запускаем браузер бещ GUI (без графической оболочки)
options.add_argument(r"user-data-dir=C:\Users\moonz\AppData\Local\Google\Chrome",)
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=options)


driver.get("https://www.youtube.com/feed/history/search_history")  # Переходим на страницу с историей поиска


def coments():
    try:

        for i in range(1, 500):  # При итерации на 500 получил 4208
            driver.set_page_load_timeout(30)
            driver.execute_script("window.scrollTo(0,100000000000000);")  # Прокрутка страницы вниз

            time.sleep(2)

        b = driver.find_elements_by_xpath("//div[@id='dismissable']/a/div")

        text = str()
        # Записываем получкенные данные в файл
        for i in b:
            text += i.text + '\n'
        with open('poisk.txt', 'a', encoding='utf-8') as c:
            c.writelines(text)


    finally:
        driver.close()  # Закрываем бразуер, завершаем процесс.


coments()
