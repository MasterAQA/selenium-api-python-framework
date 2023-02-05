import base64
import json
import time

import pytest
import requests
from selenium.webdriver.common.by import By
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

from api_urls import api_urls
from api_client.api_client import ApiClient
from selenium_locators import sel_locators
from selenium_pages.home_page import HomePage
from selenium_pages.blog_page import BlogPage
from selenium_pages.login_page import LoginPage


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
    driver.get(sel_locators.MY_ACCOUNT)
    time.sleep(2)
    driver.find_element(sel_locators.USERNAME_LOGIN).send_keys(user)
    driver.find_element(sel_locators.PASSWORD_LOGIN).send_keys(password)
    driver.find_element(sel_locators.LOGIN_BUTTON).click()
    time.sleep(2)
    assert driver.find_element(sel_locators.WELCOME_GOOD).is_displayed()
    cookies = driver.get_cookies()
    driver.quit()
    return cookies[0]

    # base_page.get_url(sel_locators.MY_ACCOUNT)
    # base_page.find_element((By.XPATH, sel_locators.USERNAME)).send_keys(user)
    # base_page.find_element((By.XPATH, sel_locators.PASSWORD)).send_keys(password)
    # base_page.find_element((By.XPATH, sel_locators.LOGIN_BUTTON)).click()
    # assert base_page.find_element((By.XPATH, sel_locators.MY_ACC_CONTENT)).is_displayed()
    # cookies = base_page.driver().get_cookies()
    # new_cookie = {}
    # for cookie in cookies:
    #     new_cookie["name"] = cookie["name"]
    #     new_cookie["value"] = cookie["value"]
    # return new_cookie


@pytest.fixture()
def api_client(rest_api, woocomerce_api):
    return ApiClient(rest_api, woocomerce_api)


@pytest.fixture()
def home_page(driver, login_cookies):
    return HomePage(driver, login_cookies)


@pytest.fixture()
def posts_page(driver, login_cookies):
    return BlogPage(driver, login_cookies)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)
