import pandas as pd
import numpy as np
df = pd.read_csv("Data/weather_data_Replace.csv")
print(df)
print('##########################################')

########### Replacing single value
new_df = df.replace(-99999, value=np.NaN)
#print(new_df)

######################## Replacing list with single value
new_df = df.replace(to_replace=[-99999,-88888], value=0)
#print(new_df)


########### Replacing per column
new_df = df.replace({
        'temperature': -99999,
        'windspeed': -99999,
        'event': '0'
    }, value= np.nan)
#print(new_df)

############# Replacing by using mapping
new_df = df.replace({
        -99999: np.nan,
        'no event': 'Sunny_1',
    })
#print(new_df)


############## Regex  --- Replace alphabets or numbers from a column
# when windspeed data is 6 mph, 7 mph etc. & temperature data is 32 F, 28 F etc.
new_df = df.replace({'temperature': '[A-Za-z]', 'windspeed': '[a-z]'},'', regex=True)
#print(new_df)

############# Replacing list with another list
df = pd.DataFrame({
    'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})
print(df)

df1 = df.replace(['poor', 'average', 'good', 'exceptional'], [1,2,3,4])
print(df1)