import sirope
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def get_id(self):
        return self._username

    @staticmethod
    def current_user(srp: sirope.Sirope, username: str):
        return next(srp.find(User, lambda u: u._username == username), None)

    def check_password(self, password):
        return self._password == password
