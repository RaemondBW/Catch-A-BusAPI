#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
#from flask.ext.httpauth import HTTPBasicAuth
from resources import agencies, agencyList

app = Flask(__name__, static_url_path = "")
#auth = HTTPBasicAuth()

@app.route('/agencies', methods = ['get'])
def returnAgencies():
    return url_for('static', filename="agencies.json")
    #return jsonify({'agencies' : agencies})

@app.route('/agencyList', methods = ['get'])
def returnAgencyList():
    return url_for('static', filename="agencyList.json")
    #return jsonify({'agencyList' : agencyList})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10080)