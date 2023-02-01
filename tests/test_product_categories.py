

def test_category_decor(home_page):
    home_page.get_home_page()
    home_page.click_decor()

    assert home_page.title_category_decor()
