# Автомтазируем процесс раскрутки за счет добавления чужого кала(творчества) в Избранное =)
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox('D:\profile')
        self.driver.implicitly_wait(10)


    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.deviantart.com/newest/")
        driver.find_element_by_xpath("//div[@id='page-1-results']/span/a/span").click()
        driver.find_element_by_xpath("//div[@id='page-1-results']/span[2]/a/span").click()
        driver.find_element_by_xpath("//div[@id='page-1-results']/span[3]/a/span").click()
        driver.find_element_by_xpath("//div[@id='page-1-results']/span[4]/a/span").click()




if __name__ == "__main__":
    unittest.main()
