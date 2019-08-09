from selenium import webdriver


class SeleniumDriver(object):

    @staticmethod
    def driver():
        driver = webdriver.Chrome()
        return driver
