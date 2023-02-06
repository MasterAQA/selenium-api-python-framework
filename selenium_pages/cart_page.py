import time
from random import randint

from selenium_pages.base_page import BasePage
from selenium_locators import sel_locators as l


class CartPage(BasePage):
    def __init__(self, driver, login_cookies):
        super().__init__(driver)
        self.get_page()
        self._driver.add_cookie(login_cookies)

    def get_page(self):
        self.get_url(l.CART_PAGE)

    def get_shop_page(self):
        self.get_url(l.SHOP_PAGE)

    def add_product_random(self):
        id_product = randint(223, 232)
        if id_product >= 229:
            id_product += 1
        print(id_product)
        self.actionChains.move_to_element(
            self.wait_for(
                *((l.HOVER_PRODUCT[0], l.HOVER_PRODUCT[1].format(id_product)))
            )
        ).perform()
        time.sleep(2)
        self.find_element(
            (l.ADD_PRODUCT[0], l.ADD_PRODUCT[1].format(id_product))
        ).click()
        time.sleep(1)
