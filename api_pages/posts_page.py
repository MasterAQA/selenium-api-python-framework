import pytest

from api_pages.base_page_api import BasePageApi


@pytest.mark.usefixtures()
class PostsPageAPI(BasePageApi):
    def login_rest_api(self):
        return self.login().get("name") == "qatesting"
