import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\moonz\AppData\Local\Google\Chrome")
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=options)
driver.get("https://www.deviantart.com/newest/")


driver.find_element_by_xpath("//a[@class='torpedo-thumb-link']").click()
time.sleep(2)


def coments():  # Ищим линки на юзеров.

    a = driver.find_element_by_xpath \
        ("//div[@class='dev-view-about']").find_element_by_xpath("//span[@class='dev-title-avatar']")\
        .find_element_by_css_selector('a').get_attribute('href')
    with open('links.txt', 'a') as c:
        c.writelines(a + '\n')


    driver.find_element_by_xpath("//img[@alt='Right']").click()

    time.sleep(2)

while True:
    coments()