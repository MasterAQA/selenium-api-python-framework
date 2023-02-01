

def test_posts(post_page, post):
    post_page.get_blog_page()
    result = post_page.check_test_post()

    assert result
