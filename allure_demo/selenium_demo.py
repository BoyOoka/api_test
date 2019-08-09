import pytest
import unittest
import allure
from .sele_driver import SeleniumDriver
from selenium import webdriver


@pytest.fixture(scope='class', autouse=True)
def drivere():
    print('scope=class')
    # driver = webdriver.Chrome()
    # driver.get("https://www.baidu.com")


class TestSeleniumDemo(SeleniumDriver):

    @allure.title('开启浏览器')
    def test_open_url(self):
        self.driver().get("http://www.baidu.com")
        print(drivere)
