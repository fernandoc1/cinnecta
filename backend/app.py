#! /usr/bin/python3

import flask
import pprint

#Code that is going to Google Cloud
import receive_text

app = flask.Flask(__name__, static_url_path='', static_folder='../html/')
app.config['UPLOAD_FOLDER'] = "/tmp/upload"

@app.route('/receive_text')
def receiveText():
    print(flask.request)
    return receive_text.receive_text(flask.request)

app.run(debug=True, port=5000) #run app in debug mode on port 5000
