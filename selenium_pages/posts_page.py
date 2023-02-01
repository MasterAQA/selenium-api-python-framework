from selenium_pages.base_page import BasePage
from selenium_locators import sel_locators


class BlogPage(BasePage):
    # def __init__(self, post, driver):
    #     super().__init__(driver)
    #     self.id = post

    def get_blog_page(self):
        self.get_url(sel_locators.BLOG_PAGE)

    def check_test_post(self):
        return self.find_element(sel_locators.TEST_POST)

