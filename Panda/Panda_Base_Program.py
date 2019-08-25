import pandas as pd

df = pd.read_csv('Data/nyc_weather.csv')
print (df)

################## max temp of thr month
mx_tmp = df['Temperature'].max()
print(mx_tmp)

############## Date when it rain
DT_rn = df['EST'][df['Events']=='Rain']
print (DT_rn)

############## Mean wind speed of the month
df.fillna(0, inplace=True)
Wd_sp = df['WindSpeedMPH'].mean()
print(Wd_sp)
