
import requests
import json
import pandas as pd


import requests
import json
import pandas as pd
"""
def serverInfos () :
    
    data = requests.get("https://api.battlemetrics.com/servers/10377404")
    data = data.json()
    response = app.response_class(
    response=json.dumps(data),
    
    response = pd.json_normalize(response)
    #playerCount.to_csv(r'.\serverInfos.csv')
    return playerCount

exemple = serverInfos()
print(exemple)
    """

data = requests.get("https://api.battlemetrics.com/servers/10377404")
data = data.json()

data = json.dumps(data),
#data = pd.json_normalize(data)
print(data)