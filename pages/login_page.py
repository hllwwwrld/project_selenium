from .base_page import BasePage
from .locators import LoginPageLocators


# methods for login page
class LoginPage(BasePage):

    # check if page is actually a login page
    def should_be_login_page(self):
        assert self.is_url_contains_login(), '"Login" not in current url'
        assert self.is_login_form_present(), 'Login form is not presented'
        assert self.is_register_form_present(), 'Registration form is not presented'

    # return true if page url contains login
    def is_url_contains_login(self):
        return 'login' in self.browser.current_url

    # return true if page contains login form
    def is_login_form_present(self):
        return self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    # return true if page contains register form
    def is_register_form_present(self):
        return self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    # method to register new user on login page (takes email and password)
    def register_new_user(self, email, password):
        # finding form to fill/submit
        email_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        password_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_1)
        password_confirm_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_CONFIRM)
        registration_submit = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_SUBMIT)
        # filling forms, submit filled
        email_form.send_keys(email)
        password_form.send_keys(password)
        password_confirm_form.send_keys(password)
        registration_submit.click()



