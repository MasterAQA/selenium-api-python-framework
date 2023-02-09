from faker import Faker


class FakeData:
    def __init__(self):
        self.fake = Faker()
        self.reg_user = "test_" + self.fake.profile()["mail"]
        self.reg_user_1 = "test_" + self.fake.profile()["mail"]
        self.reg_pass = self.fake.password(12)
        self.weak_pass = self.fake.password(4)
        self.author = self.fake.first_name()
        self.post_title = self.fake.job()
        self.comment_content = self.fake.text()
        self.email = self.fake.profile()["mail"]
        self.name = self.fake.name()
        self.number = f"+7{self.fake.msisdn()[3:]}"
        self.content = self.fake.text()


FakeObjects = FakeData()
