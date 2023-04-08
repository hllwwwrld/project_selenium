from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .pages.main_page import MainPage


class TestMainPage:
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
    link = 'http://selenium1py.pythonanywhere.com/'

    def test_guest_can_see_the_login_link(self, browser):
        page = MainPage(browser, self.link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, self.link)
        page.open()
        page.go_to_login_page()



