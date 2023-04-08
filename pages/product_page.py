from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart_button.click()

    def should_be_correct_message_about_adding_product(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        add_to_cart_alert_book_name = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_ALERT_BOOK_NAME).text
        assert book_name == add_to_cart_alert_book_name, f'Book name in alert is not similar with adding book, ' \
                                                         f'expected: {book_name}, actual: {add_to_cart_alert_book_name}'

    def cart_value_should_be_equal_to_products_value(self):
        product_value = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text.split()[0]
        cart_value_after_adding_product = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_ALERT_NEW_CART_VALUE).text.split()[0]
        assert product_value == cart_value_after_adding_product, 'added product price not equal to new basket price'
