#! /usr/bin/python3

import db_connector

def getTextCollection():
    db = db_connector.getDBConnection()
    return db["text_collection"].find()

def getFullDict(dictEntry):
    textCollection = getTextCollection()
    fullDict = dict()
    for document in textCollection:
        currentDocument = document[dictEntry]
        for entry in currentDocument:
            if entry in fullDict:
                fullDict[entry] += currentDocument[entry]
            else:
                fullDict[entry] = currentDocument[entry]
    entryList = []
    amountList = []
    for entry in fullDict:
        entryList.append(entry)
        amountList.append(fullDict[entry])
    return entryList, amountList

print(getFullDict("text_dict"))
#print(getFullDict("text_2gram_dict"))

