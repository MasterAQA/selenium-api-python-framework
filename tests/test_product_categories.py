CATEGORY_ACCESSORIES = "Accessories"
CATEGORY_CLOTHING = "Clothing"
CATEGORY_DECOR = "Decor"
CATEGORY_FASHION = "Fashion"
CATEGORY_HOODIES = "Hoodies"
CATEGORY_MOST_POPULAR = "Most Popular"
CATEGORY_MUSIC = "Music"
CATEGORY_NEW_ARRIVALS = "New Arrivals"
CATEGORY_SALE_PRODUCTS = "Sale Products"
CATEGORY_TSHIRTS = "Tshirts"


def test_category_accessories(home_page):
    home_page.click_category(CATEGORY_ACCESSORIES)

    assert home_page.title_category(CATEGORY_ACCESSORIES)


def test_category_clothing(home_page):
    home_page.click_category(CATEGORY_CLOTHING)

    assert home_page.title_category(CATEGORY_CLOTHING)


def test_category_decor(home_page):
    home_page.click_category(CATEGORY_DECOR)

    assert home_page.title_category(CATEGORY_DECOR)


def test_category_fashion(home_page):
    home_page.click_category(CATEGORY_FASHION)

    assert home_page.title_category(CATEGORY_FASHION)


def test_category_hoodies(home_page):
    home_page.click_category(CATEGORY_HOODIES)

    assert home_page.title_category(CATEGORY_HOODIES)


def test_category_most_popular(home_page):
    home_page.click_category(CATEGORY_MOST_POPULAR)

    assert home_page.title_category(CATEGORY_MOST_POPULAR)


def test_category_music(home_page):
    home_page.click_category(CATEGORY_MUSIC)

    assert home_page.title_category(CATEGORY_MUSIC)


def test_category_new_arrivals(home_page):
    home_page.click_category(CATEGORY_NEW_ARRIVALS)

    assert home_page.title_category(CATEGORY_NEW_ARRIVALS)


def test_category_sale_products(home_page):
    home_page.click_category(CATEGORY_SALE_PRODUCTS)

    assert home_page.title_category(CATEGORY_SALE_PRODUCTS)


def test_category_tshirts(home_page):
    home_page.click_category(CATEGORY_TSHIRTS)

    assert home_page.title_category(CATEGORY_TSHIRTS)
