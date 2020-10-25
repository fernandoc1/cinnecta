#! /usr/bin/python3

import flask
import pprint

#Code that is going to Google Cloud
import receive_text
import query_text
import clear_database

app = flask.Flask(__name__, static_url_path='', static_folder='../html/')

@app.route('/receive_text', methods=['GET', 'POST'])
def receiveText():
    print(flask.request)
    return receive_text.receive_text(flask.request)

@app.route('/query_text', methods=['GET', 'POST'])
def queryText():
    print(flask.request)
    return query_text.query_text(flask.request)

@app.route('/clear_database', methods=['GET', 'POST'])
def clearDatabase():
    print(flask.request)
    return clear_database.clear_database(flask.request)

app.run(debug=True, port=5000) #run app in debug mode on port 5000
