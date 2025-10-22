from selenium import webdriver


class TestExample: # Тестовый сьют, где находятся все тесты в контексте сьюта

    # Locators

    USERNAME_FIELD = ("xpath", "//input[@id='userName']")
    EMAIL_FIELD = ("xpath", "//input[@id='userEmail']")
    CURRENT_ADDRESS_FIELD = ("xpath", "//textarea[@id='currentAddress']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    OUTPUT_BLOCK = ("xpath", "//div[@id='output']")

    # Тестовый метод (Тест)

    def test_valid_data(self):
        driver = webdriver.Chrome()
        driver.get("https://demoqa.com/text-box")

        username = driver.find_element(*self.USERNAME_FIELD)
        username.send_keys("Maga")
        assert username.get_attribute("value") == "Maga"

        email = driver.find_element(*self.EMAIL_FIELD)
        email.send_keys("maga@gmail.com")
        assert email.get_attribute("value") == "maga@gmail.com"

        address = driver.find_element(*self.CURRENT_ADDRESS_FIELD)
        address.send_keys("Gagarina 10")
        assert address.get_attribute("value") == "Gagarina 10"

        driver.find_element(*self.SUBMIT_BUTTON).click()

        output = driver.find_element(*self.OUTPUT_BLOCK)
        assert output.is_displayed() is True
        assert ("Maga" and "maga@gmail.com" and "Gagarina 10") in output.text


        # pytest - запускает все тестовые сьюты и тесты в директории
        # pytest -s - показывает принты, -s означает show
        # pytest -v - это расширенный лог, можно и желательно нужно использовать вместе с -s (-sv)
        # pytest - test/(тут указываю название тестового сьюта) - используется для запуска определенного тестового сьюта, именно python файла, пример tests/test_login.py
        # pytest -m - это запуск маркированных тестов, -m означает mark, после -m обязательно нужно указать маркировку тестов пример (pytest -sv -m smoke)
        # pytest -m "smoke or profile" - это пример нескольких маркеров которые запустятся как тесты, через or можно добавлять сколько угодно маркеров
        # pytest --lf - это перезапуск последних упавших тестов, --lf означает last failed, пример (pytest -sv --lf)
        # pytest --reruns=3 (где число после = означает кол-во перезапусков) - это кол.во перезапусков упавших тестов прежде чем показать что он упал (FAILED), после чего продолжатся другие тесты
        # pytest --maxfail=2 (где число после = означает кол-во упавших тестов, после чего нужно останавливать дальнейшие тесты) - это кол.во тестов которые допускаются к падению, если превысить значение - дальнейшие тесты не продолжатся