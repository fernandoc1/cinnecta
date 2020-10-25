import flask
import pymongo
import pprint

def receive_text(request):
    client = pymongo.MongoClient("mongodb+srv://cinnecta:9041cinnecta@cluster0.79yxn.mongodb.net/weebah?retryWrites=true&w=majority")
    db = client.test
    textCollection = db["text_collection"]
    
    jsonDict = request.get_json()
    text = jsonDict['text']

    textDict = dict()
    text2GramDict = dict()
    tokens = text.split()
    for i, tok in enumerate(tokens):
        tok = tok.replace('.', '').replace(',', '').lower()
        if tok in textDict:
            textDict[tok] += 1
        else:
            textDict[tok] = 1
        if (i+1) == len(tokens):
            continue
        tok2 = tokens[i+1].replace('.', '').replace(',', '').lower()
        entry2Gram = tok + " " + tok2
        if entry2Gram in text2GramDict:
            text2GramDict[entry2Gram] += 1
        else:
            text2GramDict[entry2Gram] = 1

    #print(textDict)
    #print(text2GramDict)

    textCollection.insert_one({"title": jsonDict['title'], "text_dict": textDict, "text_2gram_dict": text2GramDict})

    response = flask.Response('{"response": "ok"}')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = "GET,HEAD,OPTIONS,POST,PUT"
    response.headers['Access-Control-Allow-Headers'] = "Origin, X-Requested-With, Content-Type, Accept, Authorization";
    response.headers['Content-Type'] = 'application/json'
    return response

