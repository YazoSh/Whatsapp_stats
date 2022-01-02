from flask import Flask, request, jsonify
from flask import Flask
from flask_cors import CORS, cross_origin

from helpers import sendData

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api', methods=['POST'])
def api():
	return jsonify(sendData(request.files['file']))
