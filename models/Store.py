from db import db


class StoreModel(db.Model):
    # tell sql alchemy about the table
    __tablename__ = 'stores'

    # cols that table contains
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # lazy=dynamic - turns items into a query builder instead of a list
    items = db.relationship('ItemModel', lazy='dynamic')  # list of ItemModels

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    # with sql alchemy this method does either update or insert
    def save_to_db(self):
        # we can add multiple rows to the session and do one commit at the end
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  # SELECT * FROM items WHERE name=name LIMIT 1
