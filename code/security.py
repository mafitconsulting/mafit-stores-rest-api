from werkzeug.security import safe_str_cmp  # flask safe way of comparing strings
from models.user import UserModel



def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):  # flask safe way of comparing strings
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)

