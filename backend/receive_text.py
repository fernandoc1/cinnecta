import flask

def receive_text(request):
    jsonDict = request.get_json()
    text = jsonDict['text']

    textDict = dict()
    text2GramDict = dict()
    tokens = text.split()
    for i, tok in enumerate(tokens):
        if tok in textDict:
            textDict[tok] += 1
        else:
            textDict[tok] = 1
        if (i+1) == len(tokens):
            continue
        entry2Gram = tokens[i] + " " + tokens[i+1]
        if entry2Gram in text2GramDict:
            text2GramDict[entry2Gram] += 1
        else:
            text2GramDict[entry2Gram] = 1

    print(textDict)
    print(text2GramDict)

    response = flask.Response('{"response": "ok"}')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = "GET,HEAD,OPTIONS,POST,PUT"
    response.headers['Access-Control-Allow-Headers'] = "Origin, X-Requested-With, Content-Type, Accept, Authorization";
    response.headers['Content-Type'] = 'application/json'
    return response

