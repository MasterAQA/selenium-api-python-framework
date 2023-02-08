from configuration import user, password
from faker import Faker


CORRECT_USER = user
CORRECT_PASS = password
REG_USER = "test_" + Faker().profile()["mail"]
REG_PASS = Faker().password(12)


def test_login_rest_api(api_client):

    assert api_client.about_me()


def test_login_correct(login_page):
    login_page.login(CORRECT_USER, CORRECT_PASS)

    assert login_page.good_login()


def test_login_incorrect(login_page):
    login_page.login(REG_USER, REG_PASS)

    assert login_page.error_login()
