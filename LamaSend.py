# Отправляем лам в подарок :3
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Users\moonz\AppData\Local\Google\Chrome")
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=options)
driver.get("https://takadk.deviantart.com/")

def send():
    time.sleep(2)
    driver.find_element_by_xpath("//div[@id='deviant']/div/div[3]/a[3]/span").click()
    time.sleep(2)
    driver.find_element_by_xpath("//body[@id='deviantART-v7']/div/div/div/a[3]/span").click()
    time.sleep(5)
    driver.switch_to.frame('badges_iframe')
    driver.find_element_by_xpath("//input[@value='Give']").click()

send()