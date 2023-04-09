from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > .btn[href$='/basket/']")
    LOGOUT_LINK = (By.CSS_SELECTOR, '#logout_link')



class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form')
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, '#register_form #id_registration-email')
    REGISTER_FORM_PASSWORD_1 = (By.CSS_SELECTOR, '#register_form #id_registration-password1')
    REGISTER_FORM_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#register_form #id_registration-password2')
    REGISTER_FORM_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ADD_TO_CART_SUCCESS_MESSAGE_BOOK_NAME = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    ADD_TO_CART_SUCCESS_MESSAGE_CART_VALUE = (By.CSS_SELECTOR, '#messages > div  p > strong')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_page div > h1')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_page div > .price_color')
    ADD_TO_CURT_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > .alert-success')


class BasketPageLocators:
    BASKET_SUMMARY = (By.CSS_SELECTOR, '#content_inner > .basket_summary')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
