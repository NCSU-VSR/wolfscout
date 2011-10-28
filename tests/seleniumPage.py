from selenium.common.exceptions import NoSuchElementException, TimeoutException
from wolfscoutException import WolfScoutException

__author__ = 'bo'

class SeleniumPage():
    _driver = None
    _waiter = None

    def isElementPresent(self, id):
        try:
            SeleniumPage._driver.find_element_by_id(id)
            return True
        except NoSuchElementException:
            return False

    def waitFor(self, condition):
        SeleniumPage._waiter.until(lambda driver: condition())

    def __init__(self, driver, waiter):
        SeleniumPage._driver = driver
        SeleniumPage._waiter = waiter