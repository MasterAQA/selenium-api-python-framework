from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from configuration import BASE_URL

# Ненавистный Overlay
overlay = (By.XPATH, "//div[@class='open_shop_overlayloader']")


HOME_PAGE = BASE_URL
LOGIN_PAGE = f"{BASE_URL}/my-account/"
BLOG_PAGE = f"{BASE_URL}/blog/"
MY_ACCOUNT = f"{BASE_URL}/my-account/"


USERNAME_LOGIN = (By.XPATH, "//input[@id='username']")
PASSWORD_LOGIN = (By.XPATH, "//input[@id='password']")
LOGIN_BUTTON = (By.XPATH, "//button[contains(@class,'login__submit')]")
WELCOME_GOOD = (By.XPATH, "//div[@class='woocommerce-MyAccount-content']")
WELCOME_ERROR = (By.XPATH, "//ul[@class='woocommerce-error']")
ALREADY_REG = (
    By.XPATH,
    "//ul[@class='woocommerce-error']/li[contains(text(), 'уже зарегистрирована')]",
)

USERNAME_REG = (By.XPATH, "//input[@id='reg_email']")
PASSWORD_REG = (By.XPATH, "//input[@id='reg_password']")
REG_BUTTON = (By.XPATH, "//button[contains(@class,'register__submit')]")


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
