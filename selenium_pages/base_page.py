from selenium.webdriver import ActionChains
from selenium_locators.sel_locators import overlay
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from configuration import BASE_URL


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 30)
        self.actionChains = ActionChains(driver)
        self.default_url = BASE_URL
        self.overlay = overlay

    def driver(self):
        return self._driver

    def wait_for(self, *locator: dict) -> WebDriver:
        return self._wait.until(ec.presence_of_element_located(locator))

    def _wait_for_overlay(self, locator: dict) -> dict:
        self._wait.until(ec.invisibility_of_element_located(self.overlay))
        self._wait.until(ec.presence_of_element_located(locator))
        self._wait.until(ec.visibility_of_element_located(locator))
        return locator

    def find_element(self, locator) -> WebElement:
        return self._driver.find_element(*(self._wait_for_overlay(locator)))

    def get_url(self, url: str):
        self._driver.get(url)
