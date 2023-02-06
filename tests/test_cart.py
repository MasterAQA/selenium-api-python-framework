import time


def test_cart(api_client, cart_page):
    cart_page.get_shop_page()
    cart_page.add_product_random()
    time.sleep(2)
    cart_page.add_product_random()
    time.sleep(2)
