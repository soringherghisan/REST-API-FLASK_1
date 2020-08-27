from flask_sqlalchemy import SQLAlchemy

from db import db


class UserModel(db.Model):
    # tell sql alchemy about the table
    __tablename__ = 'users'

    # cols that table contains - name of vars become the actual names of the db table
    id = db.Column(db.Integer, primary_key=True)  # primary key auto increments
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        # self.id = _id  # id is a python keyword
        self.username = username
        self.password = password

    def save_to_db(self):
        # we can add multiple rows to the session and do one commit at the end
        db.session.add(self)
        db.session.commit()

    # def delete_from_db(self):
    #     db.session.delete(self)
    #     db.session.commit()

    # add ability to retrieve stuff from db
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


"""
------------ code before adding sqlalchemy

class UserModel():
    def __init__(self, _id, _username, _passw):
        self.id = _id  # id is a python keyword
        self.username = _username
        self.password = _passw

    # add ability to retrieve stuff from db
    @classmethod
    def find_by_username(cls, username):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))  # params always have to be in form of a touple
        row = result.fetchone()
        if row:
            # user = cls(row[0], row[1], row[2])  # rewrite below
            user = cls(*row)
        else:
            user = None

        conn.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))  # params always have to be in form of a touple
        row = result.fetchone()
        if row:
            # user = cls(row[0], row[1], row[2])  # rewrite below
            user = cls(*row)
        else:
            user = None

        conn.close()
        return user


"""
