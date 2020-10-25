#! /usr/bin/python3

import db_connector

def getData():
    db = db_connector.getDBConnection()
    cursor = db["text_collection"].find()
    for document in cursor:
        print(document)

getData()

