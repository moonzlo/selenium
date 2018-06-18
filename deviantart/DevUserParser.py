#!/home/moonz/PycharmProjects/selenium/venv/bin/python3

from selenium import webdriver
import time

start = time.time()




def coments():  # Ищим линки на юзеров.
    """Смысл функции был в том что бы каждый раз полностью завершать работу хромдрайвера,
    данный подход снизил нагрузку на оперативную память (даёт передышку) между запусками цикла."""

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument(r"user-data-dir=/home/moonz/profile")
    driver = webdriver.Chrome(executable_path="/home/moonz/webdrivers/chromedriver", chrome_options=options)

    driver.get("https://www.deviantart.com/newest/")

    driver.find_element_by_xpath("//a[@class='torpedo-thumb-link']").click()
    time.sleep(1)

    scetchik = int(0)  # Для подсчёта Успешно добавленных линков.

    try:
        for i in range(50):

            a = driver.find_element_by_xpath \
                ("//div[@class='dev-view-about']").find_element_by_xpath("//span[@class='dev-title-avatar']")\
                .find_element_by_css_selector('a').get_attribute('href')

            with open('links.txt', 'r+') as c:
                prov = c.readlines()  # Читаем все строки.

                if str(a + '\n') not in prov:  # Реализуем проверку вхождений линка в списке.
                    c.writelines(a + '\n')
                    scetchik += 1
                else:
                    continue


            driver.find_element_by_xpath("//img[@alt='Right']").click()

            time.sleep(1)


    except Exception as error:
        print('ОШИБКА ! | ',error)

    finally:
        driver.close()
        time.sleep(2)
        driver.quit()
        time.sleep(2)
        return 'Было добавлено: {}'.format(scetchik)



for i in range(10000):
    a = coments()
    print('закончил цикл |', a)
    time.sleep(200)


print(time.time() - start)
