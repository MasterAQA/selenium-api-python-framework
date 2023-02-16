import base64
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from woocommerce import API

from selenium import webdriver
from configuration import (
    app_name,
    app_pass,
    consumer_key,
    consumer_secret,
    BASE_URL,
    user,
    password,
)

from api_client.api_client import ApiClient
from selenium_pages import sel_locators as l
from selenium_pages.account_page import AccountPage
from selenium_pages.home_page import HomePage
from selenium_pages.blog_page import BlogPage
from selenium_pages.login_page import LoginPage
from selenium_pages.cart_page import CartPage
from selenium_pages.contact_us_page import ContactUsPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()

    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def rest_api():
    credentials = app_name + ":" + app_pass
    token = base64.b64encode(credentials.encode())
    headers = {"Authorization": "Basic " + token.decode("utf-8")}
    return headers


@pytest.fixture(scope="session")
def woocomerce_api():
    wcapi = API(
        url=BASE_URL,  # Your store URL
        consumer_key=consumer_key,  # Your consumer key
        consumer_secret=consumer_secret,  # Your consumer secret
        wp_api=True,  # Enable the WP REST API integration
        version="wc/v3",  # WooCommerce WP REST API version
    )
    return wcapi


@pytest.fixture(scope="session")
def login_cookies():
    driver = webdriver.Firefox()
    driver.get(l.MY_ACCOUNT)
    WebDriverWait(driver, 10).until(ec.invisibility_of_element_located(l.overlay))
    driver.find_element(*l.USERNAME_LOGIN).send_keys(user)
    driver.find_element(*l.PASSWORD_LOGIN).send_keys(password)
    driver.find_element(*l.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(ec.invisibility_of_element_located(l.overlay))
    assert driver.find_element(*l.WELCOME_GOOD).is_displayed()
    cookies = driver.get_cookies()
    driver.quit()
    return cookies[0]


@pytest.fixture()
def api_client(rest_api, woocomerce_api):
    return ApiClient(rest_api, woocomerce_api)


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)


@pytest.fixture()
def account_page(driver, login_cookies):
    return AccountPage(driver, login_cookies)


@pytest.fixture()
def blog_page(driver):
    return BlogPage(driver)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture()
def contact_us_page(driver):
    return ContactUsPage(driver)
