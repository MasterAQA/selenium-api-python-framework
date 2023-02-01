import json

import requests
from api_locators import api_locators


class BasePageApi:
    def __init__(self, headers, wcapi):
        self._headers = headers
        self._wcapi = wcapi

    def login(self):
        response = requests.get(api_locators.about_me, headers=self._headers)
        return json.loads(response.content)
