"""

section 6 - about SQL Alchemy -
    - ORM - Object relational mapping


so far:
    flask, flask-restful, flask-jwt, flask-sqlalchemy



-- about folder structure and maintainability
    - folders in python are called packages
    - to make a package, add __init__ file

app/
- models (database stuff)
- resources (API resources )




- about models -
    - internal representation of an entity

- about resources -
    - things the APIs deals with
    - students, items, etc....

    - external representation of an entity

"""

# 3rd party
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

### own files
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

######################################################################################################################

app = Flask(__name__)

# define type of db and path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# only changes extensions behaviour and not underlying sql alchemy behaviour
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # flask-alchemy can track changes and takes resources

app.secret_key = 'secret'
api = Api(app)

jwt = JWT(app, authenticate, identity)

# add resources to Api ; endpoints
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    # importing here in order to avoid circular imports - since models are going to import db as well
    from db import db

    db.init_app(app)
    app.run(debug=True)
