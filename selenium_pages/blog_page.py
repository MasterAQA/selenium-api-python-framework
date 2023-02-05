from selenium_pages.base_page import BasePage
from selenium_locators import sel_locators as l


class BlogPage(BasePage):
    def __init__(self, driver, login_cookies):
        super().__init__(driver)
        self.get_blog_page()
        self._driver.add_cookie(login_cookies)
        # self._driver.refresh()

    def get_blog_page(self):
        self.get_url(l.BLOG_PAGE)

    def check_test_post(self, title="Test"):
        return self.find_element((l.TEST_POST[0], l.TEST_POST[1].format(title)))
