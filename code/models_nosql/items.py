from extensions import mongo


class ItemCollection():

    @classmethod
    def addItem(cls):
        items_collection = mongo.db.items

    @classmethod
    def getAll(cls):
        items_collection = mongo.db.items
        return list(items_collection.find({}))
