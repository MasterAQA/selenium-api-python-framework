from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from configuration import BASE_URL

# Ненавистный Overlay
overlay = (By.XPATH, "//div[@class='open_shop_overlayloader']")


HOME_PAGE = BASE_URL
BLOG_PAGE = "http://host1853931.hostland.pro/blog/"
MY_ACCOUNT = "http://host1853931.hostland.pro/my-account/"


USERNAME = "//input[@id='username']"
PASSWORD = "//input[@id='password']"
LOGIN_BUTTON = "//button[contains(@class,'login__submit')]"
MY_ACC_CONTENT = "//div[@class='woocommerce-MyAccount-content']"

SELECT_CATEGORY_DECOR = (
    By.XPATH,
    "//ul[@class='product-cat-list thunk-product-cat-list']//a[contains(text(), 'Decor')]",
)
TITLE_CATEGORY_DECOR = (
    By.XPATH,
    "//h1[@class='thunk-page-top-title entry-title']/span[contains(text(), 'Decor')]",
)
TEST_POST = (
    By.XPATH,
    "//h2[@class='entry-title thunk-post-title']/a[contains(text(), '{}')]",
)


