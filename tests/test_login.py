import time

from configuration import user, password

CORRECT_USER = user
CORRECT_PASS = password
REG_USER = "test_gineklo1@yandex.ru"
REG_USER_1 = "test_gineklo2@yandex.ru"
REG_PASS = "S5168wKAyiwet"
WEAK_PASS = "G1526"


def test_login_rest_api(api_client):

    assert api_client.about_me()


def test_login_correct(login_page):
    login_page.login(CORRECT_USER, CORRECT_PASS)

    assert login_page.good_login()


def test_login_incorrect(login_page):
    login_page.login(REG_USER, WEAK_PASS)

    assert login_page.error_login()
