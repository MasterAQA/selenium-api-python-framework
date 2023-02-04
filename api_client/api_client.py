from api_client.base_api_client import ApiBase
from api_urls.api_urls import ConstantsWeb


class ApiClient(ApiBase):
    def create_post(self, title="Test", status="publish", content="test_content"):
        return self.send_request(
            "POST",
            ConstantsWeb.NEW_POST,
            data={
                "title": title,
                "status": status,
                "content": content,
            },
        ).json()["id"]

    def delete_post(self, id_post):
        self.send_request("DELETE", ConstantsWeb.NEW_POST + f"/{id_post}?force=true")






    # def id_create_post(self, title="Test", status="publish", content="test_content"):
    #     return self.create_post().json()["id"]

    # response = self.session.post(api_locators.posts, headers=self._headers, data=data)
    # assert response.status_code == 201
    # id = json.loads(response.content)
