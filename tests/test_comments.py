from faker import Faker


# POST_TITLE = Faker().title()
POST_TITLE = "Beauty & Care"
COMMENT_CONTENT = Faker().text()
AUTHOR = Faker().first_name()
EMAIL = Faker().profile()["mail"]


def test_comment(api_client, blog_page):
    print(Faker().mdgen)
    id = api_client.create_post(title=POST_TITLE)
    blog_page.get_page()
    blog_page.write_comment(POST_TITLE, COMMENT_CONTENT, AUTHOR, EMAIL)

    assert blog_page.check_test_comment(COMMENT_CONTENT).is_displayed()

    api_client.delete_post(id)
