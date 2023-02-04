import json
from urllib.parse import urljoin

import requests
from api_urls.api_urls import ConstantsWeb
from configuration import root_url


class ApiBase:
    def __init__(self, headers, wcapi):
        self._headers = headers
        self._wcapi = wcapi
        self._root_url = root_url
        self.session = requests.Session()

    def about_me(self):
        response = requests.get(
            self._root_url + ConstantsWeb.ABOUT_ME, headers=self._headers
        )
        return json.loads(response.content)

    # class PostsPageAPI(BasePageApi):
    #     def login_rest_api(self):
    #         return self.login().get("name") == "qatesting"

    def send_request(self, method, path, **kwargs):
        url = self._root_url + path
        response = requests.request(method, url, headers=self._headers, **kwargs)
        assert response.status_code == 200 or 201
        return response

    def cookie_to_browser(self):
        self.session.cookies.items()
