import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Please, choose language by \'--language=\'')
    parser.addoption('--browser-name', action='store', default='chrome',
                     help='You must to write browser name with \'--browser-name=\'')


@pytest.fixture(scope='function')
def browser(request):
    lang = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        options_chr = ChromeOptions()
        options_chr.add_experimental_option('prefs', {'intl.accept_languages': lang})
        driver = webdriver.Chrome(options=options_chr, service=Service(ChromeDriverManager().install()))
    elif browser_name == 'firefox':
        options_ff = FirefoxOptions()
        options_ff.set_preference('intl.accept_languages', lang)
        driver = webdriver.Firefox(options=options_ff, service=Service(GeckoDriverManager().install()))
    else:
        raise pytest.UsageError("For '--browser-name' chrome and firefox browsers are available only")
    yield driver
    driver.quit()
