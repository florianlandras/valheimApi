import flask
from flask_cors import CORS # https://flask-cors.readthedocs.io/en/latest/
import requests
import pandas as pd
from serverData import playerNumber
from serverData import server
from flask import Flask, request, render_template, session, redirect

app = flask.Flask(__name__, template_folder="templates")
app.config["DEBUG"] = True
CORS(app)


@app.route('/', methods=["POST",'GET'])
def index():
    return render_template('index.html')

@app.route('/api', methods=["POST",'GET'])
def summary():
    return server().to_json(orient="table")

@app.route('/graph', methods=['GET'])
def graph():
    startDate = request.args.get('startDate')
    endDate = request.args.get('endDate')
    if startDate is None :
        startDate = "2021-02-27"
    if endDate is None :
        endDate = "2021-03-05"
    return playerNumber(startDate,endDate).to_json(orient="table")



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)