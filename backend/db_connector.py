import pymongo

def getDBConnection():
    client = pymongo.MongoClient("mongodb+srv://cinnecta:9041cinnecta@cluster0.79yxn.mongodb.net/weebah?retryWrites=true&w=majority")
    return client.test

