from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time


@pytest.mark.product_page
@pytest.mark.guest
class TestProductPage:

    @pytest.mark.need_review
    @pytest.mark.add_to_basket
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                      pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, link):
        product_page = ProductPage(browser=browser, url=link)  # initializing product page
        product_page.open()  # opening initialized page
        product_price = product_page.get_product_value()  # getting price of product on page
        book_name = product_page.get_book_name()  # getting name of product on page
        product_page.add_to_cart()  # adding product from page to basket
        product_page.solve_quiz_and_get_code()  # solving opened alert
        # getting message when adding product to basket
        add_to_cart_alert_book_name = product_page.get_product_name_in_add_to_cart_success_message()
        # checking if product name similar to product name in message when product added in basket (correct message)
        assert book_name == add_to_cart_alert_book_name, f'Book name in alert is not similar with adding book, ' \
                                                         f'expected: {book_name}, actual: {add_to_cart_alert_book_name}'
        # getting new value of basket after adding new product
        new_cart_value = product_page.get_cart_value_after_adding_product()
        # cheking if new value is similar to actual added product
        assert product_price == new_cart_value, 'added product price not equal to new basket price'

    @pytest.mark.add_to_basket
    @pytest.mark.xfail  # mark for test which expected fails
    @pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'])
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        product_page = ProductPage(browser=browser, url=link)
        product_page.open()
        product_page.add_to_cart()
        product_page.should_not_be_success_message()

    @pytest.mark.add_to_basket
    @pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'])
    def test_guest_cant_see_success_message(self, browser, link):
        product_page = ProductPage(browser=browser, url=link)
        product_page.open()
        # checking if product page do not contain success message without adding product to basket
        product_page.should_not_be_success_message()

    @pytest.mark.add_to_basket
    @pytest.mark.xfail
    @pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'])
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        product_page = ProductPage(browser=browser, url=link)
        product_page.open()
        product_page.add_to_cart()
        # checking if product page contain success message after adding product to basket
        product_page.success_message_should_disapper()

    @pytest.mark.login
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        # checking if giuest-user can see login button from product page
        product_page.should_be_login_link()

    @pytest.mark.need_review
    @pytest.mark.login
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()
        # initializing login page based on current url after jumping to login page (by method go_to_login_page)
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()  # checking that initialized page is actually a login page

    @pytest.mark.need_review
    @pytest.mark.add_to_basket
    @pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'])
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, link):
        product_page = ProductPage(browser, url=link)
        product_page.open()
        product_page.go_to_basket_page()  # jumping to basket page from product page (without adding products to basket)
        basket_page = BasketPage(browser, url=browser.current_url)  # initializing basket page based on current url

        # checking if product list ib basket is actually empty and having message that basket empty
        assert basket_page.is_basket_products_empty(), 'Having product in basket but not should be'
        assert basket_page.is_basket_having_message_about_empty_basket(), 'Dont have message in empty basket but should be'

    @pytest.mark.add_to_basket
    @pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'])
    def test_guest_can_see_product_in_basket_after_adding(self, browser, link):
        product_page = ProductPage(browser, url=link)
        product_page.open()
        # adding product to basket and doing same actions from test before (checking basket content according to point)
        product_page.add_to_cart()
        product_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        assert not basket_page.is_basket_products_empty(), 'Basket is empty after adding a product'
        assert not basket_page.is_basket_having_message_about_empty_basket(), 'Having empty basket message in basket' \
                                                                              'but not should be'


@pytest.mark.user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture  # executing manually in every func - register new user based on uniq time
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        login_page = LoginPage(browser=browser, url='http://selenium1py.pythonanywhere.com/ru/accounts/login/')
        login_page.open()
        login_page.register_new_user(email, password)  # on login page calling method for register new user

    # same test from guest test-suite, but for every test creating new user
    @pytest.mark.add_to_basket
    @pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'])
    def test_user_cant_see_success_message(self, browser, link, setup):
        product_page = ProductPage(browser=browser, url=link)
        product_page.open()
        # checking if test works with authorized user (created in fixture)
        assert product_page.is_user_authorized(), f'unauthorized user, email: {self.email}, password: {self.password}'
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    @pytest.mark.add_to_basket
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
    def test_user_can_add_product_to_basket(self, browser, link, setup):
        product_page = ProductPage(browser=browser, url=link)
        product_page.open()
        # checking if test works with authorized user (created in fixture)
        assert product_page.is_user_authorized(), f'unauthorized user, email: {self.email}, password: {self.password}'
        product_price = product_page.get_product_value()
        book_name = product_page.get_book_name()
        product_page.add_to_cart()
        add_to_cart_alert_book_name = product_page.get_product_name_in_add_to_cart_success_message()
        assert book_name == add_to_cart_alert_book_name, f'Book name in alert is not similar with adding book, ' \
                                                         f'expected: {book_name}, actual: {add_to_cart_alert_book_name}'
        new_cart_value = product_page.get_cart_value_after_adding_product()
        assert product_price == new_cart_value, 'added product price not equal to new basket price'
