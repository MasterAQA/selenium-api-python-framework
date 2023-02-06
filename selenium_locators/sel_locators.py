from selenium.webdriver.common.by import By

from configuration import BASE_URL

# Ненавистный Overlay
overlay = (By.XPATH, "//div[@class='open_shop_overlayloader']")

# Pages
HOME_PAGE = BASE_URL
LOGIN_PAGE = f"{BASE_URL}/my-account/"
BLOG_PAGE = f"{BASE_URL}/blog/"
MY_ACCOUNT = f"{BASE_URL}/my-account/"
CART_PAGE = f"{BASE_URL}/cart/"
SHOP_PAGE = f"{BASE_URL}/shop/"
CONTACT_US_PAGE = f"{BASE_URL}/contact-us/"

# Login page
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


# Cart page
ADD_PRODUCT = (
    By.XPATH,
    "//li[contains(@class,'post-{}')]//a[contains(@class,'add_to_cart')]",
)
HOVER_PRODUCT = (
    By.XPATH,
    "//li[contains(@class,'post-{}')]//div[@class='thunk-product']",
)


SELECT_CATEGORY_DECOR = (
    By.XPATH,
    "//ul[@class='product-cat-list thunk-product-cat-list']//a[contains(text(), 'Decor')]",
)
TITLE_CATEGORY_DECOR = (
    By.XPATH,
    "//h1[@class='thunk-page-top-title entry-title']/span[contains(text(), 'Decor')]",
)


# Post page
TEST_POST = (
    By.XPATH,
    "//h2[@class='entry-title thunk-post-title']/a[contains(text(), '{}')]",
)


# Comment page
TEXTAREA_COMMENT = (By.XPATH, "//textarea[@id='comment']")
COMMENT_SEND_BUTTON = (By.XPATH, "//input[@id='submit']")
COMMENT_CONTENT = (By.XPATH, "//div[@class='comment-content'][contains(text(), '{}')]")
INPUT_AUTHOR = (By.XPATH, "//input[@id='author']")
INPUT_EMAIL = (By.XPATH, "//input[@id='email']")

# Contact Us page
INPUT_NAME = (By.XPATH, "//input[@id='name_1']")
INPUT_EMAIL_1 = (By.XPATH, "//input[@id='email_2']")
INPUT_NUMBER = (By.XPATH, "//input[@id='number_3']")
TEXTAREA_COMMENT_1 = (By.XPATH, "//textarea[@id='message_4']")
CONTACT_US_BUTTON = (By.XPATH, "//input[@id='0']")
SUCCESS_MSG = (By.XPATH, "//p[@class='successmsg_1 successmsg']")
