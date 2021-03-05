
import requests
import json
import pandas as pd


import requests
import json
import pandas as pd

def playerNumber (startDate, endDate) :# exemple 2021-02-27 c
    startDate = startDate +'T12:00:00Z'
    endDate = endDate + 'T11:00:00Z'
    payload = {'start': startDate, 'stop': endDate}
    print(payload)
    playerCount = requests.get("https://api.battlemetrics.com/servers/10377404/player-count-history", params=payload)
    playerCount = playerCount.json()
    playerCount = pd.json_normalize(playerCount, record_path=['data'])
    playerCount.to_csv(r'.\file.csv')
    return playerCount

exemple = playerNumber(
    "2021-03-01", "2021-03-04"
)


