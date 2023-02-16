def test_logout(api_client, account_page):
    account_page.logout()

    assert account_page.check_not_logged()
