
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

def server():

    data = requests.get("https://api.battlemetrics.com/servers/10377404")
    data = data.json()
    df = pd.json_normalize(data)
    name = ['included', 'type', 'id', 'attributes.id', 'name', 'address', 'ip', 'port', 'players', 'maxPlayers', 'rank', 'location', 'status', 'serverSteamId', 'private', 'createdAt', 'updatedAt', 'portQuery', 'country', 'queryStatus', 'data.type', 'data.id']
    df.columns = name
    df = df.drop(['data.type', 'included', 'attributes.id', 'type', 'data.id'], axis=1)
    df.to_csv(r'.\file.csv')

    return df

def playerNumber (startDate='2021-02-27', endDate = '2021-03-05') :# exemple 2021-02-27
    startDate = startDate +'T00:00:00Z'
    endDate = endDate + 'T00:00:00Z'
    payload = {'start': startDate, 'stop': endDate}
    print(payload)
    playerCount = requests.get("https://api.battlemetrics.com/servers/10377404/player-count-history", params=payload)
    playerCount = playerCount.json()
    df = pd.json_normalize(playerCount, record_path=['data'])
    #Renomme les colonnes
    df = df.rename(columns={"attributes.timestamp": "date", "attributes.max" : "nombreDeJoueur"})
    # Supprimer lheure de la colonne
    #df["date"] = df["date"].str.split("T", expand=True)
    df = df.drop(["type", "attributes.value", "attributes.min"], axis = 1) #TODO enlever lindex
    df["date"] =  pd.to_datetime(df["date"],  yearfirst=True)
    #df["date"] = df["date"].apply(lambda date: date.split("T")[0])
    df = df.sort_values(by="date")
    ax = plt.gca()
    df.plot(kind='line',x='date',y='nombreDeJoueur',ax=ax)
    #plt.show()
    df.to_csv(r'.\file.csv')
    return df
