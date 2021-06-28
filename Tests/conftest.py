import pytest
import sys
sys.path.append('../')

from selenium import webdriver
from Config.config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    if request.param == "firefox":
        web_driver = webdriver.firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()