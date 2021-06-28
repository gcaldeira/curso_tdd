import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# Constants
GOOGLE_HOME = 'https://www.google.com'
GLOBO_HOME = 'https://www.globo.com'


# Scenarios
scenarios('../features/login.feature')


# Fixtures
@pytest.fixture
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    yield driver
    # driver.quit()



# Given Steps
@given('I access the site')
def open_browser(browser):
    browser.get(GOOGLE_HOME)

@given('I access the page')
def open_browser(browser):
    browser.get(GLOBO_HOME)

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.google.com")
#
# @given('I access the site')
# def blablabla(context):
#     print("Passou Aqui")