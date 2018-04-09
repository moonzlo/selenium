# Побеждаем в очередной мини игры на сложение.
# Суть игры заключаеться в том что скалдывать все числа в ума, и нажимать на верный ответ из списка ответов.
# Бот принимает числа игнорирую знаки с помощью регулярного вырожения.

import time
from selenium import webdriver
import re


options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=D:\Chrome")
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe", chrome_options=options)

driver.get("https://wikium.ru/challenge/3777/play")  # Переходим на страницу с игрой.
time.sleep(2) # Ожидаем загрузку страницы


def findNums():
    pattern = r'[0-9]+'
    # Обрабатывать исключения Обязательно.
    try:
        time.sleep(4)  # Ожидаем загрузку фрйэма.

        # Фокусируем веб драйвер на фрэйме.
        driver.switch_to.frame(driver.find_element_by_class_name('game_iframe_container'))
        # Нажимем на кнопку "Начать управжениен".
        a = driver.find_element_by_xpath(u"(//a[contains(text(),'Начать упражнение')])[2]").click()
        # Ожидаем загрузки подсказки
        time.sleep(2)
        # Кликаем на окно что бы начать игру.
        b = driver.find_element_by_xpath("//div[@class='game-screen__inner']").click()
        time.sleep(5)
        # Ждём таймер 3 секунды для загрузки задания.

        for i in range(1, 40):
            time.sleep(1.5)
            try:
                a = driver.find_element_by_xpath("//p").text
                # b = a.split()
                nums = re.findall(pattern, str(a))

                from functools import reduce
                sum_all = reduce(lambda x, y: int(x) + int(y), nums)
                print(sum_all)

                zadacha = driver.find_elements_by_xpath("//span[@class='game-math__item-inner ng-binding']")

                for i in zadacha:
                    try:
                        if i.text == str(sum_all):
                            i.click()
                    except:
                        continue

            except:
                continue


    except:
        print('Ощибка')
    finally:
        driver.close()
        time.sleep(2)
        driver.quit()
        time.sleep(2)


findNums()