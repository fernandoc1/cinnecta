import flask

def receive_text(request):
    print(request.get_json())

    response = flask.Response('{"data": "ok"}')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = "GET,HEAD,OPTIONS,POST,PUT"
    response.headers['Access-Control-Allow-Headers'] = "Origin, X-Requested-With, Content-Type, Accept, Authorization";
    response.headers['Content-Type'] = 'application/json'
    return response

