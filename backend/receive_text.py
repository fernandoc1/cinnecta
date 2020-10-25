import flask

def receive_text(request):
    jsonDict = request.get_json()
    text = jsonDict['text']

    textDict = dict()
    tokens = text.split()
    for tok in tokens:
        if tok in textDict:
            textDict[tok] += 1
        else:
            textDict[tok] = 1

    #print(textDict)

    response = flask.Response('{"response": "ok"}')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = "GET,HEAD,OPTIONS,POST,PUT"
    response.headers['Access-Control-Allow-Headers'] = "Origin, X-Requested-With, Content-Type, Accept, Authorization";
    response.headers['Content-Type'] = 'application/json'
    return response

