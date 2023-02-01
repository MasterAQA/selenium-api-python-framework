import base64
import json

import pytest
import requests
from woocommerce import API

from selenium import webdriver
from configuration import app_name, app_pass, consumer_key, consumer_secret, BASE_URL

from api_locators import api_locators
from api_pages.posts_page import PostsPageAPI
from selenium_pages.home_page import HomePage
from selenium_pages.posts_page import BlogPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()

    yield driver
    handles = driver.window_handles
    size = len(handles)
    for x in range(size):
        driver.switch_to.window(handles[x])
        driver.close()


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


@pytest.fixture()
def posts_api(rest_api, woocomerce_api):
    return PostsPageAPI(rest_api, woocomerce_api)


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)

@pytest.fixture()
def post_page(driver):
    return BlogPage(driver)


@pytest.fixture()
def post(rest_api):
    data = {
        "title": "Test",
        "status": "publish",
        "content": "test content",
    }
    response = requests.post(api_locators.posts, headers=rest_api, data=data)
    assert response.status_code == 201
    id = json.loads(response.content)
    yield
    response = requests.delete(
        api_locators.posts + f"//{id}?force=true", headers=rest_api
    )

    assert response.status_code == 200
