import pandas as pd
import numpy as np
from sklearn import linear_model


df = pd.read_csv("Data/homeprices.csv")

model = linear_model.LinearRegression()
model.fit(df[['area']],df.price)

print(model.coef_)

print(model.intercept_)

print(model.predict([[5000]]))

print('Score')
print (model.score(df[['area']], df.price))


############## Save Model To a File Using Python Pickle

import pickle
with open('SavedModel/homeprices_model_pickle','wb') as file:
    pickle.dump(model,file)

#############  Load Saved Model using pickle

with open('SavedModel/homeprices_model_pickle','rb') as file:
    mp = pickle.load(file)

print (mp.coef_)
print(mp.intercept_)
mp.predict([[5000]])

##############3#### Save Trained Model Using joblib

from sklearn.externals import joblib
joblib.dump(model, 'SavedModel/homeprices_model_joblib')

#import joblib

#################### Load Saved Model

mj = joblib.load('SavedModel/homeprices_model_joblib')

print(mj.coef_)
print(mj.intercept_)
print(
mj.predict([[5000]]))

mj = joblib.load('SavedModel/homeprices_model_joblib')
