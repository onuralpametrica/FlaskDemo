from pymongo import MongoClient


def get_database():
    connection_string = ""
    client = MongoClient(connection_string)
    return client['Register']



