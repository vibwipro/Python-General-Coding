
import pandas as pd
df = pd.read_csv("Data/weather_by_cities.csv")

g = df.groupby("city")

for city, data in g:
    print("city:",city)
    print("\n")
    print("data:",data)



############  This is similar to SQL,
###########  SELECT * from weather_data GROUP BY city

#print(g.get_group('mumbai'))


########### max temp & wind speed
#print (g.max())

############ mean of all columns
#print (g.mean())


##### min of all columns
#print(g.min())

### describe
#g.describe()

### sixe
#g.size()

### count
#g.count()

######### Ploting
g.plot()

