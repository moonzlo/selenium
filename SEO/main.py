from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class WebDriver(object):
    def __init__(self, proxy):
        self.PROXY = proxy
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')  # Запускаем бразуер бещ GUI (без графичиской оболочки)
        options.add_argument(r"user-data-dir=C:\Users\moonz\AppData\Local\Google\Chrome")
        options.add_argument('--proxy-server=%s' % self.PROXY)
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=options)


    def start(self):
        try:
            self.driver.get("https://yandex.ru/internet/")
            time.sleep(10)
        except Exception as error:
            print(error)

        finally:
            self.driver.close()
            time.sleep(2)
            self.driver.quit()
            time.sleep(2)








PROXY = '167.99.158.48:443' # Работает только с HTTPS
a = WebDriver(PROXY)
a.start()
