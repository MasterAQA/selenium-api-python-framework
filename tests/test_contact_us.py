from fake import FakeObjects as f


def test_contact_us(api_client, contact_us_page):
    contact_us_page.get_page()
    contact_us_page.send_an_application(f.name, f.email, f.number, f.content)

    assert contact_us_page.success_msg().is_displayed()
