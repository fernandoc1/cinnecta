#! /usr/bin/python3

import pymongo
import pprint

client = pymongo.MongoClient("mongodb+srv://cinnecta:9041cinnecta@cluster0.79yxn.mongodb.net/weebah?retryWrites=true&w=majority")
db = client.test

textCollection = db["text_collection"]

textCollection.insert_one({"test": "xxx"})

