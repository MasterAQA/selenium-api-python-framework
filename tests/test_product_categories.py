import time


def test_category_decor(home_page):
    # home_page.get_home_page()
    home_page.click_decor()
    time.sleep(5)
    assert home_page.title_category_decor()
