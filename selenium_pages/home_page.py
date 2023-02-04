import pytest

from selenium_pages.base_page import BasePage
from selenium_locators import sel_locators


class HomePage(BasePage):
    def __init__(self, driver, login_cookies):
        super().__init__(driver)
        self.get_home_page()
        self._driver.add_cookie(login_cookies)

    def get_home_page(self):
        self.get_url(sel_locators.HOME_PAGE)

    def click_decor(self):
        self.find_element(sel_locators.SELECT_CATEGORY_DECOR).click()

    def title_category_decor(self):
        return self.find_element(sel_locators.TITLE_CATEGORY_DECOR).is_displayed()
