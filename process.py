from config import get_database
from helpers.mongo import update_document


def get_users_from_mongo():
    collection_name = 'users'
    mongo_db = get_database()
    collection = mongo_db[collection_name]
    result = collection.find({}, {"_id": 0})
    data = list(result)
    return data


def create_name_surname(data):
    end_name = data.get('name', None)
    end_surname = data.get('surname', None)
    end_email = data.get('email', None)
    if end_name is None or end_surname is None:
        raise Exception("Name or surname is missing!")

    user = {
        "name": end_name,
        "surname": end_surname,
        "email": end_email
    }
    collection_name = 'users'
    mongo_db = get_database()
    collection = mongo_db[collection_name]

    creating_user = update_document(
        collection=collection,
        document=user
    )

    return creating_user
