from selenium.webdriver.common.by import By

from configuration import BASE_URL

# Ненавистный Overlay
overlay = (By.XPATH, "//div[@class='open_shop_overlayloader']")


HOME_PAGE = BASE_URL
BLOG_PAGE = "http://host1853931.hostland.pro/blog/"


SELECT_CATEGORY_DECOR = (By.XPATH, "//ul[@class='product-cat-list thunk-product-cat-list']//a[contains(text(), 'Decor')]")
TITLE_CATEGORY_DECOR = (By.XPATH, "//h1[@class='thunk-page-top-title entry-title']/span[contains(text(), 'Decor')]")
TEST_POST = (By.XPATH, "//h2[@class='entry-title thunk-post-title']/a[contains(text(), 'Test')]")