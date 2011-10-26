__author__ = 'bo'
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from sys import *
import loginPage
from seleniumTestConstants import *

class Tests(unittest.TestCase):
    """
    See http://readthedocs.org/docs/selenium-python/en/latest/ for Selenium Python API
    or http://seleniumhq.org/docs/03_webdriver.html for more info about Selenium and WebDriver
    """
    _driver = None
    _waiter = None
    _validUser = ("a","a")
    _validUserWrongCase = (("A", "a"),("a","A"))
    _invalidUser = ("invalid", "invalid")

    @classmethod
    def setUpClass(cls):
        cls._driver = webdriver.Firefox()
        cls._waiter = WebDriverWait(Tests._driver, TIMEOUT)

    @classmethod
    def tearDownClass(cls):
        cls._driver.quit()

    def setUp(self):
        Tests._driver.get(WOLFSCOUT_URL)
        self.loginPage = loginPage.Login(Tests._driver, Tests._waiter)

    def tearDown(self):
        Tests._driver.get(LOGOUT_URL)
        Tests._driver.get(BLANK_PAGE)

    def testLogin(self):
        self.loginPage.loginAndVerify(Tests._validUser[0], Tests._validUser[1])

    def testLogin_wrongCase(self):
        for wrongCase in Tests._validUserWrongCase:
            self.loginPage.loginToFail(wrongCase[0], wrongCase[1])

    def testLogin_badUser(self):
        self.loginPage.loginToFail(Tests._invalidUser[0], Tests._invalidUser[1])


def getDriver():
    return webdriver.Firefox()