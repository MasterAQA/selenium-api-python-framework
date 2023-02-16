from selenium_pages.base_page import BasePage
from selenium_pages import sel_locators as l


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.get_page()

    def get_page(self):
        self.get_url(l.LOGIN_PAGE)

    def login(self, email, password):
        self.find_element(l.USERNAME_LOGIN).send_keys(email)
        self.find_element(l.PASSWORD_LOGIN).send_keys(password)
        self.find_element(l.LOGIN_BUTTON).click()

    def good_login(self) -> bool:
        return self.find_element(l.WELCOME_GOOD).is_displayed()

    def error_login(self) -> bool:
        return self.find_element(l.WELCOME_ERROR).is_displayed()

    def good_registration(self, email, password):
        self.find_element(l.USERNAME_REG).send_keys(email)
        self.find_element(l.PASSWORD_REG).send_keys(password)
        self.find_element(l.REG_BUTTON).click()

    def bad_registration(self, email, password):
        self.find_element(l.USERNAME_REG).send_keys(email)
        self.find_element(l.PASSWORD_REG).send_keys(password)
        self.find_element(l.REG_BUTTON).click()

    def reg_button_available(self) -> bool:
        return self.find_element(l.REG_BUTTON).is_enabled()
