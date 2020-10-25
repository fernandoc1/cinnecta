#! /usr/bin/python3

import db_connector

def getTextCollection():
    db = db_connector.getDBConnection()
    return db["text_collection"].find()

def getFullDict(dictEntry):
    textCollection = getTextCollection()
    fullDict = dict()
    for document in textCollection:
        for entry in document[dictEntry]:
            fullDict[entry] = 1
    entryList = []
    for entry in fullDict:
        entryList.append(entry)
    return entryList

def getData():
    db = db_connector.getDBConnection()
    cursor = db["text_collection"].find()
    for document in cursor:
        print(document["title"])

#print(getFullDict("text_dict"))
print(getFullDict("text_2gram_dict"))

