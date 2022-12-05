from pymongo import MongoClient


def get_database():
    connection_string = "mongodb+srv://Oytunaa:Data-analisti-543@cluster0.qevwqxp.mongodb.net/test"
    client = MongoClient(connection_string)
    return client['Register']



