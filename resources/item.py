from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.ItemModel import ItemModel


# every resource has to be a Class
class Item(Resource):
    # reqparse
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='YOU FORGOT THE PRICE')
    parser.add_argument('store_id', type=int, required=True, help="where's the store id")

    ######################### methods below

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)  # can call a classmethod with self. i think only in class definition
        if item:
            return item.json()
        return {'message': 'item not found ey!'}, 404

    # if it's param in def - then it's /path/name
    def post(self, name):
        # if already exists - error
        if ItemModel.find_by_name(name):
            return {'message': f'An item with naem {name} already exists'}, 400  # 400 - bad request

        # improvement 1 - get json payload/body - no need since we now have reqparse
        # data = request.get_json()  # this will throw error if body isn't json or content type is not json
        # data = request.get_json(force=True)  # doesn't care about content/type header - nice but dangerous
        # data = request.get_json(silent=True)  # doesn't throw error - just returns None

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])

        # calling class method to inset item into db
        try:
            item.save_to_db()
        except Exception as e:
            return {'message': "an error occurred on db insertion"}, 500  # 500 - internal server error

        # we want to let client know that post was succesful
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': ' item deleted baby ! '}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}  # query.all() - returns all cols&rows
