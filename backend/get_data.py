#! /usr/bin/python3

import db_connector

def getTextCollection():
    db = db_connector.getDBConnection()
    return db["text_collection"].find()

def getFullDict():
    textCollection = getTextCollection()
    fullDict = []
    for document in textCollection:
        for entry in document["text_dict"]:
            fullDict.append(entry)
    return fullDict

def getData():
    db = db_connector.getDBConnection()
    cursor = db["text_collection"].find()
    for document in cursor:
        print(document["title"])

print(getFullDict())

