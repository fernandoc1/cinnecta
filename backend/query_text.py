import flask
import pprint
import get_data
import json

def query_text(request):
    option = request.args.get('option')

    responseData = {}
    if option == "full_text_dict":
        responseData = get_data.getFullDict("text_dict")
    elif option == "full_text_2gram_dict":
        responseData = get_data.getFullDict("text_2gram_dict")
    elif option == "n_dict_text_dict":
        responseData = get_data.getNDict("text_dict")
    elif option == "n_dict_text_2gram_dict":
        responseData = get_data.getNDict("text_2gram_dict")

    responseDict = dict()
    responseDict["response"] = responseData

    response = flask.Response(json.dumps(responseDict))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = "GET,HEAD,OPTIONS,POST,PUT"
    response.headers['Access-Control-Allow-Headers'] = "Origin, X-Requested-With, Content-Type, Accept, Authorization";
    response.headers['Content-Type'] = 'application/json'
    return response

