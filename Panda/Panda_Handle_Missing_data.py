import pandas as pd

df = pd.read_csv("Data/weather_data_Missing.csv")
print(df)
print ('######################################################')


############ parse_dates convert string to date
df = pd.read_csv("Data/weather_data_Missing.csv",parse_dates=['day'])
type(df.day[0])
#print(df)

############ net day as index
##########3 inplace update original DF
df.set_index('day',inplace=True)
#print (df)


########### fill default value for n.a for all field
new_df = df.fillna(0)
#print(new_df)

#### default value for each field
new_df = df.fillna({
        'temperature': 0,
        'windspeed': 0,
        'event': 'No Event'
    })
#print(new_df)

########### forward fill value
new_df = df.fillna(method="ffill")
#print(new_df)

########### backword fill value
new_df = df.fillna(method="bfill")
#print(new_df)

######## define axis
new_df = df.fillna(method="bfill", axis="columns") # axis is either "index" or "columns"
#print(new_df)

##### linit no of filling
new_df = df.fillna(method="ffill",limit=1)
#print(new_df)

###### interpolate or guess missing value
new_df = df.interpolate()
#print(new_df)

########## interpolate in relation to time
new_df = df.interpolate(method="time")
#print(new_df)

###### drop NA
new_df = df.dropna()
#print(new_df)

############# drop filed which has all NA
new_df = df.dropna(how='all')
print(new_df)
#
########### drop records which dont have 1 valid value
new_df = df.dropna(thresh=1)
print(new_df)