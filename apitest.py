import flask
from flask import Flask, request, render_template, session, redirect
import requests
import json
import pandas as pd

data = requests.get("https://api.battlemetrics.com/servers/10377404")
data = data.json()

df = pd.json_normalize(data)
df



app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=["POST",'GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
@app.route('/api', methods=["POST",'GET'])
def html_table():
    return render_template('simple.html',  tables=[df.to_html()], titles=df.columns.values)
app.run()