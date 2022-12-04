from pymongo import MongoClient


def update_document(collection, document):
    try:
        collection.update_one({"name": document['name']}, {"$set": document}, upsert=True)
        return True
    except Exception as ex:
        print(ex)
        return False
