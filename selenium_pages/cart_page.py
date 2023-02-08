from random import randint
from selenium_pages.base_page import BasePage
from selenium_pages import sel_locators as l


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_page(self):
        self.get_url(l.CART_PAGE)

    def get_shop_page(self):
        self.get_url(l.SHOP_PAGE)

    def randint(self) -> int:
        id_product = randint(224, 232)
        if id_product >= 229:
            id_product += 1
        return id_product

    def random_list_products(self, count_int) -> set:
        new_set = set()
        while len(new_set) != count_int:
            id_product = self.randint()
            new_set.add(id_product)
        return new_set

    def add_product(self, list_products):
        for id_product in list_products:

            element = self.find_element(
                (l.HOVER_PRODUCT[0], l.HOVER_PRODUCT[1].format(id_product))
            )

            self.driver().execute_script("arguments[0].scrollIntoView(true);", element)
            self.actionChains.move_to_element(element).perform()

            self.find_element(
                (l.ADD_PRODUCT[0], l.ADD_PRODUCT[1].format(id_product))
            ).click()
            self.find_element(l.CLOSE_CART_MENU).click()

    def cart_size(self) -> int:
        return len(self.find_elements(l.CART_SIZE))

    def cart_remove_product(self):
        size = self.cart_size()
        self.find_element(
            (l.REMOVE_PRODUCT[0], l.REMOVE_PRODUCT[1].format(size))
        ).click()
