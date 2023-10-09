from App.models import User
from App.database import db

# Creates a new user given a username and password
def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()

# Gets all users in the database as a JSON object
def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.to_json() for user in users]
    return users

# Gets all users in the database
def get_all_users():
    return User.query.all()