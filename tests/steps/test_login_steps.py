from pytest_bdd import scenarios, when, then, given
from selenium import webdriver

scenarios('../features/login.feature')


@given('I access the site')
def access_site(webdriver):
    webdriver.get("https://www.google.com")