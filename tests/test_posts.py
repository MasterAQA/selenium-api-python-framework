import time

POST_TITLE_1 = "Красота и уход за лицом"
POST_TITLE_2 = "Что купить в новый год мужу"
POST_TITLE_3 = "Новый весенний комплект одежды"
CONTENT_POST = "test_content"


def test_post(api_client, blog_page):
    id = api_client.create_post(title=POST_TITLE_1)
    blog_page.get_page()

    assert blog_page.check_test_post(title=POST_TITLE_1).is_displayed()

    api_client.delete_post(id)


def test_posts(api_client, blog_page):
    id_1 = api_client.create_post(title=POST_TITLE_2)
    id_2 = api_client.create_post(title=POST_TITLE_3)
    blog_page.get_page()

    assert blog_page.check_test_post(title=POST_TITLE_2).is_displayed()
    assert blog_page.check_test_post(title=POST_TITLE_3).is_displayed()

    api_client.delete_post(id_1)
    api_client.delete_post(id_2)
