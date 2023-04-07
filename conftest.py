from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as mozzillaOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


# создание функции для того, чтобы принимать опцию --browser_name в консоли
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help='Choose browser: chrome or mozilla (default chrome)')
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: en(gb)/ru/ko... (default en)')


# фикстура для создания браузера
@pytest.fixture
def browser(request):
    # это выполнится перед указанном в scope периоде
    language = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')  # получаю параметр browser_name

    if browser_name == 'chrome':
        print(f"\nStart chrome browser with language {language} for test...")
        options_chrome = chromeOptions()
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options_chrome)

    elif browser_name == 'mozilla':
        options_firefox = mozzillaOptions()
        options_firefox.set_preference('intl.accept_languages', language)
        print(f"\nStart mozilla browser for test with language {language}...")
        browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options_firefox)

    else:
        options_chrome = chromeOptions()
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': language})
        print(f'\nChosen browser not available. Available browser names: mozilla/chrome')
        print(f"\nStart chrome browser for test BY DEFAULT with language {language}...")
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options_chrome)

    yield browser  # статья на хабре про yield https://habr.com/ru/post/132554/

    # этот код выполнится после завершения указанного периода в scope
    print("\nquit chrome browser..")
    browser.quit()
