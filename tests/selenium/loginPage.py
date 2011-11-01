from selenium.selenium import selenium

__author__ = 'bo'

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import seleniumPage
from wolfscoutException import WolfScoutException
import time

class Login(seleniumPage.SeleniumPage):
    _loginFormId = "loginForm"
    _userNameFieldID = "id_username"
    _passwordFieldID = "id_password"
    _messageElementName = "message"
    _loginFailedMessageID = "loginFailed"

    def loginAndVerify(self, userName, password):
        self.login(userName, password)
        self.verifyLoggedIn()

    def login(self, userName, password):
        self.typeInUserNameField(userName)
        self.typeInPasswordField(password)
        self.submitLoginForm()

    def loginToFail(self, userName, password):
        self.login(userName, password)
        self.verifyNotLoggedIn()

    def verifyLoggedIn(self):
        try:
            self.waitFor(self.loginSucceeded)
        except TimeoutException:
            raise WolfScoutException("Login failed")

    def verifyNotLoggedIn(self):
        try:
            self.waitFor(self.loginFailed)
        except TimeoutException:
            raise WolfScoutException("Login succeeded")

    def loginSucceeded(self):
        return self.isLoginFormDisplayed() == False

    def loginFailed(self):
        return self.isLoginFailedMessageDisplayed()

    def typeInUserNameField(self, userName):
        userNameField = Login._driver.find_element_by_id(Login._userNameFieldID)
        userNameField.send_keys(userName)

    def typeInPasswordField(self, password):
        userNameField = Login._driver.find_element_by_id(Login._passwordFieldID)
        userNameField.send_keys(password)

    def submitLoginForm(self):
        loginForm = self.getLoginForm()
        loginForm.submit()

    def getLoginForm(self):
        return Login._driver.find_element_by_id(Login._loginFormId)

    def isLoginFormDisplayed(self):
        return self.isElementPresent(Login._loginFormId)

    def isLoginFailedMessageDisplayed(self):
        return self.isElementPresent(Login._loginFailedMessageID)

    def getMessage(self):
        return Login._driver.find_element_by_id(Login._messageElementName).text()