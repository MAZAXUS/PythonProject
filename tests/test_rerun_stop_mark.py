from selenium import webdriver
import pytest

class TestRerunStopMark:


    def setup_method(self):
        self.driver = webdriver.Chrome()


    @pytest.mark.smoke
    def test_open_login_page(self):
        self.driver.get("https://demoqa.com/login")
        assert self.driver.current_url == "https://demoqa.com/login"


    @pytest.mark.smoke
    def test_open_books(self):
        self.driver.get("https://demoqa.com/books")
        assert self.driver.current_url == "https://demoqa.com/books"


    @pytest.mark.profile
    def test_open_profile(self):
        self.driver.get("https://demoqa.com/profile")
        assert self.driver.current_url == "https://demoqa.com/profile"

    def teardown_method(self):
        self.driver.quit()