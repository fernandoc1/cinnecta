import flask
import pprint
import db_connector

def clear_database(request):
    db = db_connector.getDBConnection()
    textCollection = db["text_collection"]

    textCollection.drop()

    response = flask.Response('{"response": "ok"}')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = "GET,HEAD,OPTIONS,POST,PUT"
    response.headers['Access-Control-Allow-Headers'] = "Origin, X-Requested-With, Content-Type, Accept, Authorization";
    response.headers['Content-Type'] = 'application/json'
    return response

