# Собираем историю поисковых коментариев на youtube.

import time, csv
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')  # Запускаем бразуер бещ GUI (без графичиской оболочки)
options.add_argument(r"user-data-dir=C:\Users\moonz\AppData\Local\Google\Chrome",)
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=options)


driver.get("https://www.youtube.com/feed/history/comment_history")

def read(text):
    with open('coments.csv', 'a') as f:
        write = csv.writer(f)
        write.writerow([text])

def coments():
    try:

        time.sleep(2)  # Даём странице ПОЛНОСТЬЮ прогрузиться.
        for i in range(1, 1000):  # Количество прокруток, если поставить больше 1000 получаем синий экарн :3
            driver.set_page_load_timeout(30)
            driver.execute_script("window.scrollTo(0,100000000000000);")
            # Скролим ДО значения которого всегда больше результата, иначе процесс будет прерван.
            time.sleep(2)  # Нужно немножечко поспать =)

        # Поиск только по текусту
        b = driver.find_elements_by_css_selector("div[class='style-scope ytd-expander']")
        # Поиск по целому содержанию.
        # b = driver.find_elements_by_xpath("//div[@id='content']")
        for i in b:
            # Обработаем исключение на тот случай если в тексте коментария были недопустимые символы.
            try:
                read(i.text)  # Приводим каждый объект к значению text и передаем его в функцию записи.
            except:
                continue

    finally:
        driver.close()  # Обязательно выключаем веб драйвер. (иначе он виснит в процессах)


coments()
