from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, 'bob', 'sdf')
]

username_mapping = { u.username for u in users}
userid_mapping = { u.id for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping[user_id].get(user_id, None)