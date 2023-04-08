from .pages.main_page import MainPage
from .pages.login_page import LoginPage


class TestMainPage:
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
    link = 'http://selenium1py.pythonanywhere.com/'

    def test_guest_can_see_the_login_link(self, browser):
        page = MainPage(browser, self.link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, self.link)
        page.open()

        # 1 вариант переключению на страницу логина - возврат страницы в методе,
        # где кликаем по ссылке со страницей логина
        # login_page = page.go_to_login_page()
        # login_page.should_be_login_page()

        # 2 вариант инициализация новой страницы на основании url, который получен после клика по кнопке авторизации
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
