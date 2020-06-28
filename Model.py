import pickle
import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#------------------------------------------------------------------
with open("Serialized/data.p", 'rb') as f:
    data = pickle.load(f)
    tmpData = []

with open("Serialized/target.p", 'rb') as f:
    target = pickle.load(f)
    newTarget = []

#------------------------------------------------------------------
#Hack - input data as floats in DataGen
for i, lin in enumerate(data):
    try:
        tmpData.append(lin.astype(np.float))
        newTarget.append(float(target[i]))
    except:
        pass

data = np.array(tmpData)
target = np.array(newTarget)

train_x, test_x, train_y, test_y = train_test_split(data, target)

xgb = xgb.XGBClassifier()
xgb.fit(train_x, train_y)

print(xgb)
y_pred = xgb.predict(test_x)
accuracy = accuracy_score(test_y, y_pred)

print("Accuracy: %.2f" % (accuracy))

with open("Serialized/model.p", 'wb') as f:
    pickle.dump(xgb, f)
