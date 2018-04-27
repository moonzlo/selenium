from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time


prox = Proxy()
prox.proxy_type = ProxyType.MANUAL

prox.ssl_proxy = "167.99.3.74:53"




capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

options = webdriver.ChromeOptions()
#options.add_argument('headless')  # Запускаем бразуер бещ GUI (без графичиской оболочки)
options.add_argument(r"user-data-dir=C:\Users\moonz\AppData\Local\Google\Chrome")
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=options, desired_capabilities=capabilities)





try:
    driver.get("https://yandex.ru/internet/")
    time.sleep(100)
    driver.get("https://metal52.ru")
except Exception as error:
    print(error)

finally:
    driver.close()
    time.sleep(2)
    driver.quit()
    time.sleep(2)