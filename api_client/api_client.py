from api_client.base_api_client import ApiBase


class ApiClient(ApiBase):
    def create_post(self, title="Test", status="publish", content="test_content"):
        return self.send_request(
            "POST",
            self.path.NEW_POST,
            data={
                "title": title,
                "status": status,
                "content": content,
            },
        ).json()["id"]

    def delete_post(self, id_post):
        self.send_request("DELETE", self.path.NEW_POST + f"/{id_post}?force=true")

    def reg_new_user(self, email, password):
        return self.send_request(
            "POST",
            self.path.NEW_USER,
            data={
                "username": email,
                "email": email,
                "password": password,
            },
        ).json()["id"]

    def search_id_user(self, username):
        if "@" in username:
            username = username.split("@")[0]
        return self.send_request("GET", self.path.SEARCH_USER.format(username),).json()[
            0
        ]["id"]

    def delete_user(self, id_user):
        response = self.send_request(
            "DELETE",
            self.path.DELETE_USER.format(id_user),
        )
        assert response.status_code == 200

    # def id_create_post(self, title="Test", status="publish", content="test_content"):
    #     return self.create_post().json()["id"]

    # response = self.session.post(api_locators.posts, headers=self._headers, data=data)
    # assert response.status_code == 201
    # id = json.loads(response.content)
