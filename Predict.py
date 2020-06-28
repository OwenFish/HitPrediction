import pickle
import pandas as pd
import numpy as np
import statsapi

matchups_file = open("matchups.csv", 'r')
matchups_file.readline()

with open("Serialized/model.p", 'rb') as f:
    model = pickle.load(f)




def getHittingData(batterID):
    try:
        r = statsapi.player_stat_data(batterID, group="hitting", type="career")["stats"][0]['stats']
        return [r['avg'], r['slg'], r['strikeOuts']]
    except IndexError:
        return None

def getPitchingData(pitcherID):
    try:
        r = statsapi.player_stat_data(pitcherID, group="pitching", type="career")['stats'][0]['stats']
        return [r['avg'], r['obp'], r['homeRunsPer9']]
    except IndexError:
        return None

data = []
for lin in matchups_file:
    lin = lin.strip().split(',')
    batterID = lin[0]
    batterName = lin[1]
    pitcherID = lin[2]
    pitcherName = lin[3]

    data.append(getHittingData(batterID) + getPitchingData(pitcherID))


data = np.array(data)
predictions = model.predict(data)

data = pd.DataFrame(data)
data['Pred'] = predictions

data.to_csv("predictions.csv")
