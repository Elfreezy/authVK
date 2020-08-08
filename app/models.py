from flask_login import UserMixin, logout_user

from app import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    token = db.Column(db.String(240))
    user_id = db.Column(db.Integer, unique=True, index=True)
    image = db.Column(db.String(240))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))