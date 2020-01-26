from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'store not found'}, 404

    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'message': "store already exist with name {}".format(name)}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except e:
            return {'message': 'error saving the store'}, 500
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'deleted'}, 204


class StoreList(Resource):

    def get(self):
        stores = StoreModel.get_all_stores()
        return {'stores': [store.json() for store in stores]}
