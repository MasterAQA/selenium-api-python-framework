from faker import Faker


NAME = Faker().name()
EMAIL = Faker().profile()["mail"]
NUMBER = f"+7{Faker().msisdn()[3:]}"
CONTENT = Faker().text()


def test_contact_us(api_client, contact_us_page):
    contact_us_page.get_page()
    contact_us_page.send_an_application(NAME, EMAIL, NUMBER, CONTENT)

    assert contact_us_page.success_msg().is_displayed()
