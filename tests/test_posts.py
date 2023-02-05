import time

CONTENT_POST = "test_content"


def test_posts(api_client, posts_page):
    id = api_client.create_post(title="Beauty2")
    # posts_page.get_blog_page()
    time.sleep(2)
    assert posts_page.check_test_post(title="Beauty2").is_displayed()

    api_client.delete_post(id)


def test_posts1(api_client, posts_page):
    id = api_client.create_post(title="Beauty1")
    # posts_page.get_blog_page()
    time.sleep(2)
    assert posts_page.check_test_post(title="Beauty1").is_displayed()

    api_client.delete_post(id)
