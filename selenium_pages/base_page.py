import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# from conftest import login_cookies

from selenium_locators.sel_locators import overlay
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from configuration import BASE_URL
import requests


class BasePage():
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)
        self.actionChains = ActionChains(driver)
        self.default_url = BASE_URL
        self.overlay = overlay

    # def login_cookies(self):
    #     self._driver.get("http://host1853931.hostland.pro/my-account/")
    #     self.find_element((By.XPATH, "//input[@id='username']")).send_keys("qatesting")
    #     self.find_element((By.XPATH, "//input[@id='password']")).send_keys("kVWydHZs@p)RX^^NBQ")
    #     self.find_element((By.XPATH, "//button[contains(@class,'login__submit')]")).click()
    #     assert self.find_element((By.XPATH, "//div[@class='woocommerce-MyAccount-content']")).is_displayed()
    #     return self._driver.get_cookies()

    def driver(self):
        return self._driver

    def wait_for(self, *locator: dict) -> WebDriver:
        return self._wait.until(ec.presence_of_element_located(locator))

    def _wait_for_overlay(self, locator: dict) -> dict:
        self._wait.until(ec.invisibility_of_element_located(self.overlay))
        self._wait.until(ec.presence_of_element_located(locator))
        return locator

    def find_element(self, locator) -> WebElement:
        return self._driver.find_element(*(self._wait_for_overlay(locator)))

    def get_url(self, url: str):
        self._driver.get(url)

    # def web_authorize(self):
    #     cookies = requests.getfixturevalue('get_cookies')
    #     new_cookie = {}
    #     for cookie in cookies:
    #         new_cookie["name"] = cookie["name"]
    #         new_cookie["value"] = cookie["value"]
    #     self._driver.add_cookie(new_cookie)
    #     self._driver.refresh()