from faker import Faker


REG_USER = "test_" + Faker().profile()["mail"]
REG_USER_1 = "test_" + Faker().profile()["mail"]
REG_PASS = Faker().password(12)
WEAK_PASS = Faker().password(4)


def test_reg_correct(api_client, login_page):
    login_page.good_registration(REG_USER, REG_PASS)
    # api_delete_user(REG_USER)

    id_user = api_client.search_id_user(REG_USER)

    try:
        assert login_page.good_login()
    finally:
        api_client.delete_user(id_user)


# def    test_fake():
#     print(REG_USER)
#     print(REG_USER_1)
#     print(REG_PASS)
#     print(WEAK_PASS)


def test_acc_already_reg(api_client, login_page):
    id_user = api_client.reg_new_user(REG_USER_1, REG_PASS)

    try:
        login_page.good_registration(REG_USER_1, REG_PASS)

        assert login_page.reg_button_available()
        assert login_page.error_login()
    finally:
        api_client.delete_user(id_user)


def test_reg_weak_pass(login_page):
    login_page.bad_registration(REG_USER, WEAK_PASS)

    assert not login_page.reg_button_available()
