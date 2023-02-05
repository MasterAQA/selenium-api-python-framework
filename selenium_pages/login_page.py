from selenium_pages.base_page import BasePage
from selenium_locators import sel_locators


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.get_page()

    def get_page(self):
        self.get_url(sel_locators.LOGIN_PAGE)

    def login(self, email, password):
        self.find_element(sel_locators.USERNAME_LOGIN).send_keys(email)
        self.find_element(sel_locators.PASSWORD_LOGIN).send_keys(password)
        self.find_element(sel_locators.LOGIN_BUTTON).click()

    def good_login(self) -> bool:
        return self.find_element(sel_locators.WELCOME_GOOD).is_displayed()

    def error_login(self) -> bool:
        return self.find_element(sel_locators.WELCOME_ERROR).is_displayed()

    def good_registration(self, email, password):
        self.find_element(sel_locators.USERNAME_REG).send_keys(email)
        self.find_element(sel_locators.PASSWORD_REG).send_keys(password)
        self.find_element(sel_locators.REG_BUTTON).click()

    def bad_registration(self, email, password):
        self.find_element(sel_locators.USERNAME_REG).send_keys(email)
        self.find_element(sel_locators.PASSWORD_REG).send_keys(password)
        self.find_element(sel_locators.REG_BUTTON).click()

    def reg_button_available(self) -> bool:
        return self.find_element(sel_locators.REG_BUTTON).is_enabled()
