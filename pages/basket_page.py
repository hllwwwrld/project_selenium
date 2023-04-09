from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_page(self):
        pass

    def is_basket_having_message_about_empty_basket(self):
        return self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE)

    def is_basket_products_empty(self):
        return self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY)

