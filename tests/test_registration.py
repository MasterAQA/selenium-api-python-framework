REG_USER = "test_ginezis@yandex.ru"
REG_USER_1 = "test_gineklo3@yandex.ru"
REG_PASS = "S5168wKAyiwet"
WEAK_PASS = "G1"


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
