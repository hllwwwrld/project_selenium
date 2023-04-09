from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.product_page
class TestProductPage:

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
        product_page = ProductPage(browser=browser, url=link)
        product_page.open()
        product_price = product_page.get_product_value()
        book_name = product_page.get_book_name()
        product_page.add_to_cart()
        product_page.solve_quiz_and_get_code()
        add_to_cart_alert_book_name = product_page.get_product_name_in_add_to_cart_success_message()
        assert book_name == add_to_cart_alert_book_name, f'Book name in alert is not similar with adding book, ' \
                                                         f'expected: {book_name}, actual: {add_to_cart_alert_book_name}'
        new_cart_value = product_page.get_cart_value_after_adding_product()
        assert product_price == new_cart_value, 'added product price not equal to new basket price'

    @pytest.mark.add_to_basket
    @pytest.mark.xfail
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
        product_page.should_not_be_success_message()

    @pytest.mark.add_to_basket
    @pytest.mark.xfail
    @pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'])
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        product_page = ProductPage(browser=browser, url=link)
        product_page.open()
        product_page.add_to_cart()
        product_page.success_message_should_disapper()

    @pytest.mark.login
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_login_link()

    @pytest.mark.login
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.add_to_basket
    @pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'])
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, link):
        product_page = ProductPage(browser, url=link)
        product_page.open()
        product_page.go_to_basket_page()
        basket_page = BasketPage(browser, url=browser.current_url)
        assert basket_page.is_basket_products_empty(), 'Having product in basket but not should be'
        assert basket_page.is_basket_having_message_about_empty_basket(), 'Dont have message in empty basket but should be'

    @pytest.mark.add_to_basket
    @pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'])
    def test_guest_can_see_product_in_basket_after_adding(self, browser, link):
        product_page = ProductPage(browser, url=link)
        product_page.open()
        product_page.add_to_cart()
        product_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        assert not basket_page.is_basket_products_empty(), 'Basket is empty after adding a product'
        assert not basket_page.is_basket_having_message_about_empty_basket(), 'Having empty basket message in basket' \
                                                                              'but not should be'