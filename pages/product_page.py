from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
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

    def get_product_value(self):
        product_value = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text.split()[0]
        return product_value

    def get_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        return book_name

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart_button.click()

    def get_cart_value_after_adding_product(self):
        cart_value_after_adding_product = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_SUCCESS_MESSAGE_CART_VALUE).text.split()[0]
        return cart_value_after_adding_product

    def get_product_name_in_add_to_cart_success_message(self):
        add_to_cart_alert_book_name = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_SUCCESS_MESSAGE_BOOK_NAME).text
        return add_to_cart_alert_book_name

    def get_success_message(self):
        success_message = self.browser.find_element(*ProductPageLocators.ADD_TO_CURT_SUCCESS_MESSAGE)
        return success_message

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_CURT_SUCCESS_MESSAGE), \
            "Success message is presented but not should be"

    def success_message_should_disapper(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_CURT_SUCCESS_MESSAGE), \
            'Success message is not disappered'

    # def should_be_correct_message_about_adding_product(self):
    #     book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
    #     add_to_cart_alert_book_name = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_ALERT_BOOK_NAME).text
    #     assert book_name == add_to_cart_alert_book_name
    #
    # def cart_value_should_be_equal_to_products_value(self):
    #     product_value = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text.split()[0]
    #     cart_value_after_adding_product = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_ALERT_NEW_CART_VALUE).text.split()[0]
    #     assert product_value == cart_value_after_adding_product
