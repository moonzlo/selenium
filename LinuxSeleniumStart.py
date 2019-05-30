from selenium import webdriver
"""Данная конфигурация реализует базовую настройку с использованием профиля пользователя """

options = webdriver.ChromeOptions()
options.add_argument('headless')  # Без GUI
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument(r"user-data-dir=/home/moonz/profile")
driver = webdriver.Chrome(executable_path="/home/moonz/chromedriver", chrome_options=options)


import pickle
"""
Библиотека для работы с куками
"""


pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))  # Пишем куки в файл
and later to add them back:

cookies = pickle.load(open("cookies.pkl", "rb"))  # Читаем куки из файла
for cookie in cookies:
    driver.add_cookie(cookie)
