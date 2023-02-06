from selenium_pages.base_page import BasePage
from selenium_locators import sel_locators as l


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.get_page()

    def get_page(self):
        self.get_url(l.HOME_PAGE)

    def click_category(self, category):
        self.find_element(
            (l.SELECT_CATEGORY[0], l.SELECT_CATEGORY[1].format(category))
        ).click()

    def title_category(self, category):
        return self.find_element(
            (l.TITLE_CATEGORY[0], l.TITLE_CATEGORY[1].format(category))
        ).is_displayed()
