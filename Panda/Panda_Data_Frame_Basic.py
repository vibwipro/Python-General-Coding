import pandas as pd
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
}
df = pd.DataFrame(weather_data)
df = pd.read_csv("Data/weather_data.csv")
print(df)

### Shape
print(df.shape)

##### print records
print (df.head(6) )

###### print trailer records
print(df.tail(7))

#### print between 1 and 3
print (df[1:3])

### print colums
print (df.columns)

### print a specific column
print (df['day']) # or df.day

### print type of data
print (type(df['day']))


## print 2 columns
print (df[['day','temperature']])

##### Max vlue in column
print (df['temperature'].max())

### print records with temp > 32
print (df[df['temperature']>32])


###### print day column for temp = max
print (df['day'][df['temperature'] == df['temperature'].max()]) # Kinda doing SQL in pandas


###### print all columns column for temp = max
print (df[df['temperature'] == df['temperature'].max()]) # Kinda doing SQL in pandas

###### print standard deviation
print (df['temperature'].std())


#### List of Panda Functions
#### https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html

##### it will print count, min, mean, std, max.
print (df.describe())


