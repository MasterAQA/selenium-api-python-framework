import time

from configuration import user, password

CORRECT_USER = user
CORRECT_PASS = password
REG_USER = "test_gineklo2@yandex.ru"
REG_USER_1 = "test_gineklo2856@yandex.ru"
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


def test_reg_correct(api_client, login_page):
    login_page.good_registration(REG_USER, REG_PASS)
    id_user = api_client.search_id_user(REG_USER)

    assert login_page.good_login()

    api_client.delete_user(id_user)


def test_acc_already_reg(api_client, login_page):
    id_user = api_client.reg_new_user(REG_USER_1, REG_PASS)
    login_page.good_registration(REG_USER_1, REG_PASS)

    assert login_page.reg_button_available()
    assert login_page.error_login()

    api_client.delete_user(id_user)


def test_reg_weak_pass(login_page):
    login_page.bad_registration(REG_USER, WEAK_PASS)

    assert login_page.reg_button_available() == False
