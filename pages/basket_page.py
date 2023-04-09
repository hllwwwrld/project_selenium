from .base_page import BasePage
from .locators import BasketPageLocators


# methods to work with basket page
class BasketPage(BasePage):

    # return true if basket having message about empty-basket
    def is_basket_having_message_about_empty_basket(self):
        return self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE)

    # return true if basket do not contain any products
    def is_basket_products_empty(self):
        return self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY)

