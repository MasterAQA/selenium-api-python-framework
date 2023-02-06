import time

NAME = "Vadim"
EMAIL = "garmornin@yandex.ru"
NUMBER = "+7901904839"
CONTENT = "Test content in contact us area"


def test_contact_us(api_client, contact_us_page):
    contact_us_page.get_page()
    contact_us_page.send_an_application(NAME, EMAIL, NUMBER, CONTENT)

    assert contact_us_page.success_msg().is_displayed()
