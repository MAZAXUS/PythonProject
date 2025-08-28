# Упрощенный вариант для автотеста страницы авторизации

class LoginPage:


    _PAGE_URL = "https://lk.staging.appgrade.pro/login"
    _LOGIN_FIELD = "//input1"
    _PASSWORD_FIELD = "//input2"

    def open(self):
        print(f"Открытие страницы {self._PAGE_URL}")


    def enter_login(self, login):
        print(f"Логин '{login}' введен в поле {self._LOGIN_FIELD}")


    def enter_password(self, password):
        print(f"Пароль '{password}' введен в поле {self._PASSWORD_FIELD}")


login_page = LoginPage()
login_page.open()
login_page.enter_login("k1eisky")
login_page.enter_password("vlasek")
