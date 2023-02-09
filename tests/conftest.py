import pytest
from fake import FakeObjects as f


@pytest.fixture()
def api_delete_user(api_client):
    yield
    id_user = api_client.search_id_user(f.reg_user)
    api_client.delete_user(id_user)


@pytest.fixture()
def api_reg_new_user(api_client):
    id_user = api_client.reg_new_user(f.reg_user_1, f.reg_pass)
    yield
    api_client.delete_user(id_user)


@pytest.fixture()
def api_new_post(api_client):
    id_post = api_client.create_post(title=f.post_title)
    yield
    api_client.delete_post(id_post)
