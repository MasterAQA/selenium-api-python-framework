def test_login(api_client, home_page):

    assert api_client.about_me()
    # home_page.get_home_page()
    # Авторизации не происходит, нужно перебрасывать куки
