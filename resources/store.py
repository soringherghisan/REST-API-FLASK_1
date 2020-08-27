from flask_restful import Resource, reqparse
# from flask_jwt import jwt_required

from models.Store import StoreModel


class Store(Resource):
    # reqparse
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=True, help='id should auto increment')
    parser.add_argument('name', type=str, required=True, help="where's the store id")

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': "Store not found"}, 404

    def post(self, name):
        # check if store alredy exists
        if StoreModel.find_by_name(name):
            return {'message': f'Store {name} already there'}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'failure on db save when creating new store'}, 500

        return store.json(), 201  # 201 - created success

    def delete(self, name):
        # check if store exists
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
