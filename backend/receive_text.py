import flask
import pprint
import db_connector

def filterString(s):
    return s.replace('.', '').replace(',', '').lower()

def receive_text(request):
    db = db_connector.getDBConnection()
    
    textCollection = db["text_collection"]
    
    jsonDict = request.get_json()
    text = jsonDict['text']

    textDict = dict()
    text2GramDict = dict()
    tokens = text.split()
    for i, tok in enumerate(tokens):
        tok = filterString(tok) 
        if tok in textDict:
            textDict[tok] += 1
        else:
            textDict[tok] = 1
        if (i+1) == len(tokens):
            continue
        tok2 = filterString(tokens[i+1])
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

