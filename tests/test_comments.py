from fake import FakeObjects as f


def test_comment(api_client, blog_page, api_new_post):
    blog_page.get_page()
    blog_page.write_comment(f.post_title, f.comment_content, f.author, f.email)

    assert blog_page.check_test_comment(f.comment_content).is_displayed()
