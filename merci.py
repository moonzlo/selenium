from contextlib import contextmanager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver import ActionChains
import time


@contextmanager
def selen(driver_patch: str, profile_patch: str, config='windows') -> webdriver.Chrome:
    """
    Самый удобный метод использования веб драйвера =)
    :param driver_patch: str: patch to chromedriver(exe)
    :param profile_patch: str: the path to the folder storing cookies
    :param config: str: operating system
    :return: webdriver.Chrome
    """

    def windows_conf():
        options = webdriver.ChromeOptions()
        options.add_argument(f'user-data-dir={profile_patch}')
        driver = webdriver.Chrome(executable_path=driver_patch, chrome_options=options)
        return driver

    def linux_conf():
        options = webdriver.ChromeOptions()
        arguments = ('headless', '--no-sandbox', '--disable-dev-shm-usage', f'user-data-dir={profile_patch}')
        for option in arguments:
            options.add_argument(option)

        driver = webdriver.Chrome(executable_path=driver_patch, chrome_options=options)
        return driver

    configs = {'windows': windows_conf, 'linux': linux_conf}
    web_driver = configs.get(config)()

    try:
        yield web_driver
        web_driver.close()
        time.sleep(1)
        web_driver.quit()

    except Exception as error:
        web_driver.close()
        time.sleep(1)
        web_driver.quit()
        raise Exception(error)


with selen(r'C:\chromedriver.exe', 'C:\profile') as browser:
    # Стартовая страница
    browser.get('http://nnmclub.to/forum/portal.php?c=10')

    def get_all_posts_page() -> list:
        # Получаем все ссылки на посты внутри одной страницы.

        p = browser.find_elements_by_xpath('//a[@class="pcomm tit-b bold"]')
        posts = []

        for i in p:
            posts.append(i.get_attribute("href"))

        # Переход на следующую страницу
        browser.find_element_by_link_text(u"След.").click()
        return posts


    def scrapy_links(iter:int) -> list:
        # Принимаем число страниц которые нужно собрать, отадёт список ссылок.
        good_list = []
        for page in range(iter):
            good_list.extend(get_all_posts_page())

        return good_list


    def thanks():
        # Ищет на странице кнопку спасибо, если она есть и не нажата то нажимает.

        try:
            bottom = browser.find_element_by_xpath(u"//img[@alt='Спасибо']")
            bottom.click()

        except NoSuchElementException:
            pass


    def main():
        all_link = scrapy_links(10)
        for i in all_link:
            browser.get(i)
            thanks()

    main()
