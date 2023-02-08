import json

import requests
from api_client.constants import ConstantsWeb
from configuration import root_url


class ApiBase:
    def __init__(self, headers, wcapi):
        self._headers = headers
        self._wcapi = wcapi
        self._root_url = root_url
        self.session = requests.Session()
        self.path = ConstantsWeb

    def about_me(self):
        response = requests.get(
            self._root_url + self.path.ABOUT_ME, headers=self._headers
        )
        response.raise_for_status()
        return json.loads(response.content)

    def send_request(self, method, path, **kwargs):
        url = self._root_url + path
        response = requests.request(method, url, headers=self._headers, **kwargs)
        response.raise_for_status()
        return response
