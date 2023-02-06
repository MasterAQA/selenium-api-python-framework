POST_TITLE = "Beauty & Care"
COMMENT_CONTENT = "Test comment content"
AUTHOR = "Jandarma"
EMAIL = "Gvatemal@yandex.ru"


def test_comment(api_client, blog_page):
    id = api_client.create_post(title=POST_TITLE)
    blog_page.get_page()
    blog_page.write_comment(POST_TITLE, COMMENT_CONTENT, AUTHOR, EMAIL)

    assert blog_page.check_test_comment(COMMENT_CONTENT).is_displayed()

    api_client.delete_post(id)
