#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
#from flask.ext.httpauth import HTTPBasicAuth
from resources import agencies

app = Flask(__name__, static_url_path = "")
#auth = HTTPBasicAuth()

@app.route('/busAPI/agencies', methods = ['get'])
def returnAgencies():
    return jsonify({'agencies' : agencies})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10080)