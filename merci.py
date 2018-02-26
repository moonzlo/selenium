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
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://nnm-club.me/forum/portal.php?c=12&start=18")
        driver.find_element_by_xpath(u"(//img[@alt='Комментарии'])[1]").click()
        driver.find_element_by_xpath(u"//img[@alt='Спасибо']").click()
        driver.back()
        driver.find_element_by_xpath(u"(//img[@alt='Комментарии'])[2]").click()
        driver.find_element_by_xpath(u"//img[@alt='Спасибо']").click()
        driver.back()
        driver.find_element_by_xpath(u"(//img[@alt='Комментарии'])[3]").click()
        driver.find_element_by_xpath(u"//img[@alt='Спасибо']").click()
        driver.back()
        driver.find_element_by_xpath(u"(//img[@alt='Комментарии'])[4]").click()
        driver.find_element_by_xpath(u"//img[@alt='Спасибо']").click()
        driver.back()
        driver.find_element_by_xpath(u"(//img[@alt='Комментарии'])[5]").click()
        driver.find_element_by_xpath(u"//img[@alt='Спасибо']").click()
        driver.back()
        driver.find_element_by_xpath(u"(//img[@alt='Комментарии'])[6]").click()
        driver.find_element_by_xpath(u"//img[@alt='Спасибо']").click()
        driver.back()
        driver.find_element_by_xpath(u"(//img[@alt='Комментарии'])[7]").click()
        driver.find_element_by_xpath(u"//img[@alt='Спасибо']").click()
        driver.back()
        driver.find_element_by_xpath(u"(//img[@alt='Комментарии'])[8]").click()
        driver.find_element_by_xpath(u"//img[@alt='Спасибо']").click()
        driver.back()
        driver.find_element_by_xpath(u"(//img[@alt='Комментарии'])[9]").click()
        driver.find_element_by_xpath(u"//img[@alt='Спасибо']").click()
        driver.back()
        driver.find_element_by_xpath(u"(//img[@alt='Комментарии'])[10]").click()
        driver.find_element_by_xpath(u"//img[@alt='Спасибо']").click()
        driver.back()
        driver.find_element_by_xpath(u"(//img[@alt='Комментарии'])[11]").click()
        driver.find_element_by_xpath(u"//img[@alt='Спасибо']").click()
        driver.back()
        driver.find_element_by_xpath(u"(//img[@alt='Комментарии'])[12]").click()
        driver.find_element_by_xpath(u"//img[@alt='Спасибо']").click()
        driver.back()
        driver.find_element_by_xpath(u"(//img[@alt='Комментарии'])[13]").click()
        driver.find_element_by_xpath(u"//img[@alt='Спасибо']").click()
        driver.back()
        driver.find_element_by_xpath(u"(//img[@alt='Комментарии'])[14]").click()
        driver.find_element_by_xpath(u"//img[@alt='Спасибо']").click()
        driver.back()
        driver.find_element_by_xpath(u"(//img[@alt='Комментарии'])[15]").click()
        driver.find_element_by_xpath(u"//img[@alt='Спасибо']").click()
        driver.back()
        driver.find_element_by_xpath(u"(//img[@alt='Комментарии'])[16]").click()
        driver.find_element_by_xpath(u"//img[@alt='Спасибо']").click()
        driver.back()
        driver.find_element_by_link_text(u"След.").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":

    unittest.main()