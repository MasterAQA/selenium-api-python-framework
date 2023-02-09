from fake import FakeObjects as f


def test_reg_correct(api_client, login_page, api_delete_user):
    login_page.good_registration(f.reg_user, f.reg_pass)

    assert login_page.good_login()


def test_acc_already_reg(api_client, login_page, api_reg_new_user):
    login_page.good_registration(f.reg_user_1, f.reg_pass)

    assert login_page.reg_button_available()
    assert login_page.error_login()


def test_reg_weak_pass(login_page):
    login_page.bad_registration(f.reg_user, f.weak_pass)

    assert not login_page.reg_button_available()
