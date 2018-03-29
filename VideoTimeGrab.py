# Собираем сумарное время роликов просмотренных на youtube.

import time
from selenium import webdriver

from bs4 import BeautifulSoup

start_time = time.time()

options = webdriver.ChromeOptions()
options.add_argument('headless')  # Запускаем бразуер бещ GUI (без графичиской оболочки)
options.add_argument(r"user-data-dir=C:\Users\moonz\AppData\Local\Google\Chrome", )
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=options)

driver.get("https://www.youtube.com/feed/history")


def videoGrabTime():
    for i in range(1, 1000):  # Количество прокруток, если поставить больше 1000 получаем синий экарн :3
        driver.set_page_load_timeout(30)
        driver.execute_script("window.scrollTo(0,100000000000000);")
        # Скролим ДО значения которого всегда больше результата, иначе процесс будет прерван.
        time.sleep(2)  # Нужно немножечко поспать =)

    time.sleep(2)
    try:
        b = driver.find_elements_by_xpath("//div[@id='overlays']/ytd-thumbnail-overlay-time-status-renderer")
        print('Всего роликов было найдено :', len(b))
        html = driver.page_source  # Получаем HTML код загруженной страницы
        spisok = []
        summ = int()

        pattern = r'\d'
        soup = BeautifulSoup(html, 'lxml')  # Создаем объект класса BeautifulSoup
        test = soup.find_all(class_='style-scope ytd-thumbnail-overlay-time-status-renderer')  # Искомое поле с цифрами

        for i in test:
            a = i.text.strip()  # Отсеиваем цифры от мусора.
            b = a.split(':')  # Разделям цифры для подсчета.
            if len(b) == 3:
                hour = int(b[0])
                minut = int(b[1])
                summ += hour * 60 + minut
                # секунды брать не будет =) мне лень :P
            elif len(b) == 2:
                minut = int(b[0])
                summ += minut
            else:  # Секундные ролики в расчет брать не будем.
                continue

        print('Минут :', summ)



    except:
        driver.close()
        driver.quit()
    finally:
        driver.close()
        driver.quit()


videoGrabTime()
print("time elapsed: {:.2f}s".format(time.time() - start_time))
