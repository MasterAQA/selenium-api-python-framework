import pytest

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


@pytest.mark.parametrize(
    "category",
    [
        CATEGORY_ACCESSORIES,
        CATEGORY_CLOTHING,
        CATEGORY_DECOR,
        CATEGORY_FASHION,
        CATEGORY_HOODIES,
        CATEGORY_MOST_POPULAR,
        CATEGORY_MUSIC,
        CATEGORY_NEW_ARRIVALS,
        CATEGORY_SALE_PRODUCTS,
        CATEGORY_TSHIRTS,
    ],
)
def test_categories(home_page, category):
    home_page.click_category(category)

    assert home_page.title_category(category)

