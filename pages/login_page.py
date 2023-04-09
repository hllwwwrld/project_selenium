from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        assert self.is_url_contains_login(), '"Login" not in current url'
        assert self.is_login_form_present(), 'Login form is not presented'
        assert self.is_register_form_present(), 'Registration form is not presented'

    def is_url_contains_login(self):
        return 'login' in self.browser.current_url

    def is_login_form_present(self):
        return self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def is_register_form_present(self):
        return self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        password_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_1)
        password_confirm_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_CONFIRM)
        registration_submit = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_SUBMIT)
        email_form.send_keys(email)
        password_form.send_keys(password)
        password_confirm_form.send_keys(password)
        registration_submit.click()



