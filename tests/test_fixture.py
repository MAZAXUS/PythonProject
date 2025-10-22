import faker
import pytest


class TestExample:

# Фикстура драйвера, чтобы в каждом тесте не инициализировать (создавать) драйвер
    @pytest.mark.usefixtures("WDI")
    def test_open_googla(self):
        self.driver.get("https://google.com")


# Использую фикстуру auth, чтобы открыть страницу Reports предварительно сделав авторизацию
    @pytest.mark.usefixtures("auth")
    def test_reports(auth):
        auth.get("https://lk.staging.appgrade.pro/reports")