import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


# class with main page tests
@pytest.mark.main_page
class TestMainPage:
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
    link = 'http://selenium1py.pythonanywhere.com/'  # declare link to work with

    @pytest.mark.login
    def test_guest_can_see_the_login_link(self, browser):
        page = MainPage(browser, self.link)  # initializing page object
        page.open()  # oppening initialized page object
        page.should_be_login_link()  # checking test point (login link enable)

    @pytest.mark.login
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, self.link)
        page.open()

        # 1 вариант переключению на страницу логина - возврат страницы в методе,
        # где кликаем по ссылке со страницей логина
        # login_page = page.go_to_login_page()
        # login_page.should_be_login_page()

        # 2 вариант инициализация новой страницы на основании url, который получен после клика по кнопке авторизации
        page.go_to_login_page()  # on initialized page object calling method to go on login page (new url opened)
        login_page = LoginPage(browser, browser.current_url)  # initializing new page object based on current url
        login_page.should_be_login_page()  # checking test point (opened page is actually login page)

    @pytest.mark.basket
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, self.link)
        page.open()
        page.go_to_basket_page()  # jumping to new page (from main page to basket page)
        basket_page = BasketPage(browser=browser, url=browser.current_url)  # initializing basket page based on current url

        # checking if basket do not contain any products and having message about empty basket

        # method to get basket products
        assert basket_page.is_basket_products_empty(), 'Having product in basket but not should be'
        # method to get empty-basket message
        assert basket_page.is_basket_having_message_about_empty_basket(), 'Dont have message in empty basket but should be'

