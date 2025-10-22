from selenium import webdriver

class TestLogin:

    def setup_method(self): # Предусловие
        self.driver = webdriver.Chrome()

    def test_open_login_page(self):
        self.driver.get("https://demoqa.com/login")
        assert self.driver.current_url == "https://demoqa.com/login", "Открыта некорректная страница"

    def teardown_method(self): # Постусловие
        self.driver.quit()