import flask
from flask import Flask, request, render_template, session, redirect
from flask_cors import CORS # https://flask-cors.readthedocs.io/en/latest/
import requests
import json
import pandas as pd
from playersCount import playerNumber
"""
data = requests.get("https://api.battlemetrics.com/servers/10377404")
data = data.json()

df = pd.json_normalize(data)
df
"""


app = flask.Flask(__name__, template_folder="templates")
app.config["DEBUG"] = True
CORS(app)


@app.route('/', methods=["POST",'GET'])
def home():
    return "a remplir"

@app.route('/api', methods=["POST",'GET'])


def summary():
    data = requests.get("https://api.battlemetrics.com/servers/10377404")
    data = data.json()
    response = app.response_class(
        response=json.dumps(data),
        mimetype='application/json'
    )
    return response

@app.route('/graph', methods=['GET'])
def graph():

    startDate = request.args.get('startDate')
    endDate = request.args.get('endDate')

    return playerNumber(startDate,endDate).to_json(orient="table")


app.run()