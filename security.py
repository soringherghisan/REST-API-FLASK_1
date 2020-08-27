"""
file contains info about authentication

- using dicts and dict.get(), we can not iterate over a list to find; hash tables ftw
"""

from models.UserModel import UserModel


######


# func to auth user - given a username and pass
def authenticate(username, password):
    # user = username_mapping.get(username, None)  # if no key with user - returns None
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user


# takes a payload ; payload is the content of the JWT, we'll extract userid and match to db
def identity(payload):
    # unique to flask jwt -
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)


"""

users = [
    User(1, 'bob', 'pass')
]

# 'bob': obj
username_mapping = {u.username: u for u in users}  # k:v comprehension
userid_mapping = {u.id: u for u in users}

"""
