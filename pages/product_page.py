from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


# methods for product pages
# subclass of base page, which initializing pages by url and web driver
class ProductPage(BasePage):
    # method for solve alert when adding promo product to basket
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # method to get price of product from page
    def get_product_value(self):
        product_value = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text.split()[0]
        # returning product price string
        return product_value

    # method to get name of product from page
    def get_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        # returning product name string
        return book_name

    # method to add product from page to basket (finding add to cart button and clicking it)
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart_button.click()

    # get new cart value in success message after adding product to basket
    def get_cart_value_after_adding_product(self):
        cart_value_after_adding_product = self.browser.find_element(
            *ProductPageLocators.ADD_TO_CART_SUCCESS_MESSAGE_CART_VALUE).text.split()[0]
        return cart_value_after_adding_product

    # get name of profuct from success message when adding product to basket
    def get_product_name_in_add_to_cart_success_message(self):
        add_to_cart_alert_book_name = self.browser.find_element(
            *ProductPageLocators.ADD_TO_CART_SUCCESS_MESSAGE_BOOK_NAME).text
        return add_to_cart_alert_book_name

    # check if page contains add to cart success message
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_CART_SUCCESS_MESSAGE), \
            "Success message is presented but not should be"

    # check if page do not contain add to cart success message
    def success_message_should_disapper(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_CART_SUCCESS_MESSAGE), \
            'Success message is not disappered'
