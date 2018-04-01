# Пишем бота для wikium турнира.
# Задача: Определить заданное число, найти его на старнице, и кликнуть по нему.
# Повторить цикл.
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\moonz\AppData\Local\Google\Chrome")
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=options)

driver.get("https://wikium.ru/challenge/3750/play")  # Переходим на страницу с игрой.
time.sleep(2)  # Ожидаем загрузку страницы


def findNums():
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

        # Запускаем цикл решения задачи.
        for set in range(1, 50):
            # Определяем какой число от нас хочет игра.
            num = driver.find_element_by_xpath \
                ("//span[@class='number-one-numbers__task-reference ng-binding ng-scope']").text
            # Получаем таблицу с числами в которых будем искать.
            setter = driver.find_elements_by_xpath\
                ("//span[@class='number-one-numbers__item-inner ng-binding']")
            # Итерируемся по списку найденых чисел.
            for i in setter:
                try:
                    if i.text == num:  # Приводим каждое полученное значение к text и сравниваем с искомым.
                        i.click()  # Если условие равно то кликаем по найденному объекту.
                    else:
                        continue
                except:
                    continue
            time.sleep(1)


    except:
        print('Ощибка')
    finally:
        driver.close()
        time.sleep(2)
        driver.quit()
        time.sleep(2)


findNums()