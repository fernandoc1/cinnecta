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
    for entry in fullDict:
        entryList.append(entry)
    return entryList

def getNDict(dictEntry):
    textCollection = getTextCollection()
    fullDict = dict()
    for document in textCollection:
        currentDocument = document[dictEntry]
        for entry in currentDocument:
            if entry in fullDict:
                fullDict[entry] += currentDocument[entry]
            else:
                fullDict[entry] = currentDocument[entry]
    documentDict = dict()
    textCollection = getTextCollection()
    for document in textCollection:
        print(document)
        currentDocument = document[dictEntry]
        wordList = []
        amountList = []
        for entry in fullDict:
            wordList.append(entry)
            if entry in currentDocument:
                amountList.append(currentDocument[entry])
            else:
                amountList.append(0)
        documentDict[document["title"]] = [wordList, amountList]
    return documentDict 

#print(getNDict("text_dict"))
#print(getFullDict("text_dict"))
#print(getFullDict("text_2gram_dict"))

