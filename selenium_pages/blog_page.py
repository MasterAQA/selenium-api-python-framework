from selenium_pages.base_page import BasePage
from selenium_locators import sel_locators as l


class BlogPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_page(self):
        self.get_url(l.BLOG_PAGE)

    def check_test_post(self, title="Test"):
        return self.find_element((l.TEST_POST[0], l.TEST_POST[1].format(title)))

    def write_comment(self, title, comment, author, email):
        self.find_element((l.TEST_POST[0], l.TEST_POST[1].format(title))).click()
        self.find_element(l.TEXTAREA_COMMENT).send_keys(comment)
        self.find_element(l.INPUT_AUTHOR).send_keys(author)
        self.find_element(l.INPUT_EMAIL).send_keys(email)
        self.find_element(l.COMMENT_SEND_BUTTON).click()

    def check_test_comment(self, content="Test comment content"):
        return self.find_element(
            (l.COMMENT_CONTENT[0], l.COMMENT_CONTENT[1].format(content))
        )
