from selenium_pages.base_page import BasePage
from selenium_pages import sel_locators as l


class AccountPage(BasePage):
    def __init__(self, driver, login_cookies):
        super().__init__(driver)
        self.get_page()
        self._driver.add_cookie(login_cookies)
        self._driver.refresh()

    def get_page(self):
        self.get_url(l.ACCOUNT_PAGE)

    def logout(self):
        self.find_element(l.LOGOUT_BUTTON).click()

    def check_not_logged(self) -> bool:
        return self.find_element(l.LOGIN_BUTTON).is_displayed()
