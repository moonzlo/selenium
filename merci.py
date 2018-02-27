from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re


class UntitledTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox('D:\profile')
        self.driver.implicitly_wait(1)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://nnm-club.me/forum/portal.php?c=19") # Целевая страница с которой начинается перебор
        while True:

            nums = int(1)
            while nums != 16: # На странице всего 16 постов, по этому цикл завершается после перебора всех 16ти
                nums1 = '[' + str(nums) + ']'
                driver.find_element_by_xpath(u"(//img[@alt='Комментарии'])" + nums1).click()
                nums += 1 # Псоле успешного перехода на страницу трекера, значение увелчивается для перехода на новую
                try:
                    driver.find_element_by_xpath(u"//img[@alt='Спасибо']").click() # проверяем не нажата ли кнопка Уже
                    driver.back() # Если НЕТ, то нажимаем и возвращаемся назад
                except:
                    driver.back() # Если Уже нажата, значит всё равно возвращаемся
            driver.find_element_by_link_text(u"След.").click() # По окончанию цикла переключаемся на следующую вкладку

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