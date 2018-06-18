# Отправляем лам в подарок :3
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\moonz\AppData\Local\Google\Chrome")
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=options)


file = open('links.txt', 'r')

def send():
    time.sleep(3)
    driver.find_element_by_xpath("//img[contains(@src,'https://st.deviantart.net/minish/gallery/down.gif')]").click()
    time.sleep(3)
    try:
        driver.find_element_by_xpath("//body[@id='deviantART-v7']/div/div/div/a[3]/span").click()
        time.sleep(4)
        driver.switch_to.frame('badges_iframe')
        driver.find_element_by_xpath("//input[@value='Give']").click()
    except:
        print('пусто')



while file != '':
    a = file.readline()
    driver.get(a)
    try:
        send()
    except:
        continue