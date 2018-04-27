from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


PROXY = '66.70.255.195:3128' # Работает только с HTTPS

options = webdriver.ChromeOptions()
#options.add_argument('headless')  # Запускаем бразуер бещ GUI (без графичиской оболочки)
options.add_argument(r"user-data-dir=C:\Users\moonz\AppData\Local\Google\Chrome")
options.add_argument('--proxy-server=%s' % PROXY)
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=options)





try:
    driver.get("https://yandex.ru/internet/")
    time.sleep(10)
except Exception as error:
    print(error)

finally:
    driver.close()
    time.sleep(2)
    driver.quit()
    time.sleep(2)