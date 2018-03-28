# Собираем сумарное время роликов просмотренных на youtube.

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('headless')  # Запускаем бразуер бещ GUI (без графичиской оболочки)
options.add_argument(r"user-data-dir=C:\Users\moonz\AppData\Local\Google\Chrome",)
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=options)


driver.get("https://www.youtube.com/feed/history")

def coments():
    try:
        action = ActionChains(driver)

        time.sleep(2)  # Даём странице ПОЛНОСТЬЮ прогрузиться.
        # Запускаем цикл прокручивания до максимального упора.
        for i in range(1, 100):  # Количество прокруток, если поставить больше 1000 получаем синий экарн :3
            driver.set_page_load_timeout(30)
            driver.execute_script("window.scrollTo(0,100000000000000);")
            # Скролим ДО значения которого всегда больше результата, иначе процесс будет прерван.
            time.sleep(2)  # Нужно немножечко поспать =)


        # Поиск минут видео
        # Ищем фрэйм с цифрами
        b = driver.find_elements_by_xpath("//div[@id='overlays']/ytd-thumbnail-overlay-time-status-renderer")
        print(len(b))

        summ = int()  # Место хранения результата.

        for i in b:  # Итерируемся по каждому найденному объекту.
            try:
                action.move_to_element(i).perform()
                # Имитируемым наведение мышки, и действие "отпускания" =)
                sp = i.text.split(':')
                if len(sp) == 3:
                    hour = int(sp[0])
                    minut = int(sp[1])
                    summ += hour * 60 + minut
                    # секунды брать не будет =) мне лень :P
                elif len(sp) == 2:
                    minut = int(sp[0])
                    summ += minut
                else:  # Секундные ролики в расчет брать не будем.
                    continue

            except:  # На всякий случай )
                continue

    finally:
        driver.close()  # Обязательно выключаем веб драйвер. (иначе он виснит в процессах)
    return print(summ)  # Возвращаем результат

coments()
