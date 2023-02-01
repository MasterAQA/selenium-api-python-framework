

def test_login(posts_api, home_page):

    assert posts_api.login()
    home_page.get_home_page()
    #Авторизации не происходит, нужно перебрасывать куки