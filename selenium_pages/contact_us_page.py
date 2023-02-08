from selenium_pages.base_page import BasePage
from selenium_pages import sel_locators as l


class ContactUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_page(self):
        self.get_url(l.CONTACT_US_PAGE)

    def send_an_application(self, name, email, number, content):
        self.find_element(l.INPUT_NAME).send_keys(name)
        self.find_element(l.INPUT_EMAIL_1).send_keys(email)
        self.find_element(l.INPUT_NUMBER).send_keys(number)
        self.find_element(l.TEXTAREA_COMMENT_1).send_keys(content)
        self.find_element(l.CONTACT_US_BUTTON).click()

    def success_msg(self):
        return self.find_element(l.SUCCESS_MSG)
