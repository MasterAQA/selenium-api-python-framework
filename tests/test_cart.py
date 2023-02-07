def test_cart_add(api_client, cart_page):
    cart_page.get_shop_page()
    id_products = cart_page.random_list_products(1)
    cart_page.add_product(id_products)
    cart_page.get_cart_page()

    assert cart_page.cart_size() == 1


def test_cart_add_multiple(api_client, cart_page):
    cart_page.get_shop_page()
    id_products = cart_page.random_list_products(3)
    cart_page.add_product(id_products)
    cart_page.get_cart_page()

    assert cart_page.cart_size() == 3


def test_cart_remove(api_client, cart_page):
    cart_page.get_shop_page()
    id_products = cart_page.random_list_products(3)
    cart_page.add_product(id_products)
    cart_page.get_cart_page()
    cart_page.cart_remove_product()

    assert cart_page.cart_size() == 2


def test_cart_remove_multiple(api_client, cart_page):
    cart_page.get_shop_page()
    id_products = cart_page.random_list_products(7)
    cart_page.add_product(id_products)
    cart_page.get_cart_page()
    [cart_page.cart_remove_product() for _ in range(3)]

    assert cart_page.cart_size() == 4
