
import requests
import json
import pandas as pd

def server():

    data = requests.get("https://api.battlemetrics.com/servers/10377404")
    data = data.json()


    #df = pd.read_json(data, orient="records")
    df = pd.json_normalize(data)

    name = ['included', 'type', 'id', 'attributes.id', 'name', 'address', 'ip', 'port', 'players', 'maxPlayers', 'rank', 'location', 'status', 'serverSteamId', 'private', 'createdAt', 'updatedAt', 'portQuery', 'country', 'queryStatus', 'data.type', 'data.id']
    df.columns = name
    df = df.drop(['data.type', 'included', 'attributes.id', 'type', 'data.id'], axis=1)
    df.to_csv(r'.\file.csv')

    return df
