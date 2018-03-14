import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\moonz\AppData\Local\Google\Chrome")
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=options)
driver.get("https://www.deviantart.com/newest/")


def coments():  # Клик на звёзжочку
    for i in range(2, 100):
        try:
            a = driver.find_element_by_xpath(
                "{}{}{}".format("// div[ @ id = 'page-1-results'] / span[", str(i), "] / a / span")).click()
            time.sleep(4)
            a.click()
        except:
            continue


coments()
