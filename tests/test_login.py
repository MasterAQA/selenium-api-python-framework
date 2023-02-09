from configuration import user, password
from fake import FakeObjects as f


CORRECT_USER = user
CORRECT_PASS = password


def test_login_rest_api(api_client):

    assert api_client.about_me()


def test_login_correct(login_page):
    login_page.login(CORRECT_USER, CORRECT_PASS)

    assert login_page.good_login()


def test_login_incorrect(login_page):
    login_page.login(f.reg_user, f.reg_pass)

    assert login_page.error_login()
