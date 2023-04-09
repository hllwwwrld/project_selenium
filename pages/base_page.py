from .locators import BasePageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# method which available for any pages
class BasePage:
    # initializing page by WebDriver and url (opening taken url in taken browser)
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # declaring implicitly wait by default or by taken value

    # opening initilized page
    def open(self):
        self.browser.get(self.url)

    # checking if page contains given element
    def is_element_present(self, method, path):
        try:
            self.browser.find_element(method, path)
        except Exception:  # if element not found returning False (element not presented on page)
            return False
        return True  # if element found returning true (element presented on page)

    # same check by method before but reversed (cheking if page do not contain given element)
    def is_not_element_present(self, method, path, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((method, path)))
        except TimeoutException:  # if element not found with given time returning true (pelements is not presented on page)
            return True
        return False  # else returng false (elements presented on page)

    # cheking if given disappered
    def is_disappeared(self, method, path, timeout=4):
        try:
            # using until not to wait until element not showing in page
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((method, path)))
        except TimeoutException:  # if element not disappeared with given time - returning false (elem still in page)
            return False
        return True  # else returning True (element disappeared from page)

    # check if page contains login link
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    # find login link and jump to login page (clock on link)
    # most of the time test initializing new page, that we are jumped to after this action
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(self.browser, self.browser.current_url)

    #  find basket link and jump to basket page (clock on link)
    # most of the time test initializing new page, that we are jumped to after this action
    def go_to_basket_page(self):
        basket_button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        basket_button.click()

    # checking if user we are working with are authorized or not
    # (returning true if user authorized false if not authorized)
    def is_user_authorized(self):
        return self.is_element_present(*BasePageLocators.LOGOUT_LINK)
