from selenium import webdriver

driver = webdriver.Firefox('D:\profile')
driver.get("https://nnm-club.me/forum/portal.php?c=16&start=1584")
while True:

    nums = int(1)

    while nums != 16:  # На странице всего 16 постов, по этому цикл завершается после перебора всех 16ти
        com = driver.find_element_by_xpath(
            u"{}{}{}{}".format("(//img[@alt='Комментарии'])", "[", str(nums), "]"))

        com.click()
        nums += 1  # Псоле успешного перехода на страницу трекера, значение увелчивается для перехода на новую

        try:
            senks = driver.find_element_by_xpath(u"//img[@alt='Спасибо']")
            senks.click()  # проверяем не нажата ли кнопка Уже
            driver.back()  # Если НЕТ, то нажимаем и возвращаемся назад
        except:
            driver.back()  # Если Уже нажата, значит всё равно возвращаемся

    driver.find_element_by_link_text(u"След.").click()