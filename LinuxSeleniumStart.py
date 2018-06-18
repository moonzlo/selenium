from selenium import webdriver
"""Данная конфигурация реализует базовую настройку с использованием профиля пользователя """

options = webdriver.ChromeOptions()
options.add_argument('headless')  # Без GUI
options.add_argument(r"user-data-dir=/home/moonz/profile")
driver = webdriver.Chrome(executable_path="/home/moonz/chromedriver", chrome_options=options)

