from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        browser.get("http://selenium1py.pythonanywhere.com/")
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()


