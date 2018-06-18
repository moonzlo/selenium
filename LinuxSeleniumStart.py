from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=/home/moonz/profile")
driver = webdriver.Chrome(executable_path="/home/moonz/chromedriver", chrome_options=options)

