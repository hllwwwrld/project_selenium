from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')


class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ADD_TO_CART_ALERT_BOOK_NAME = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    ADD_TO_CART_ALERT_NEW_CART_VALUE = (By.CSS_SELECTOR, '#messages div:nth-child(3) p > strong')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_page div > h1')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_page div > .price_color')
