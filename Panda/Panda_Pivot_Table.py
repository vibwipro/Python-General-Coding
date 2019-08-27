import pandas as pd
import numpy as np
df = pd.read_csv("Data/weather.csv")

######### print new format of DF
#print (df.pivot(index='city',columns='date'))

############ Print only humidity data with new DF
#print (df.pivot(index='city',columns='date',values="humidity"))

############ print another DF
#print (df.pivot(index='date',columns='city'))

######### another DF
print (df.pivot(index='humidity',columns='city'))