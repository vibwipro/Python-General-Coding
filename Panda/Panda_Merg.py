import pandas as pd
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})

df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})

df3 = pd.merge(df1, df2, on="city")
print (df3)

#############################################################################3
######### New DF


df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35, 38],
})

df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "humidity": [65,68,71],
})

############ Inner
df3=pd.merge(df1,df2,on="city",how="inner")
print (df3)

############ outer
df3=pd.merge(df1,df2,on="city",how="outer")
print (df3)

############ left (all records of df1)
df3=pd.merge(df1,df2,on="city",how="left")
print (df3)

############ right (all records of df2)
df3=pd.merge(df1,df2,on="city",how="right")
print (df3)


########## Indicator about type of join
df3=pd.merge(df1,df2,on="city",how="outer",indicator=True)
print(df3)


######################################################################
############# Another DF


df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35,38],
    "humidity": [65,68,71, 75]
})

df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "temperature": [21,14,35],
    "humidity": [65,68,71]
})

########## Both DF has Humidety and temp column.
########### Suffix will ass siffix to columns
df3= pd.merge(df1,df2,on="city",how="outer", suffixes=('_first','_second'))
print(df3)

############# Set city as index and update DF
######## inplace it update DF
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})
df1.set_index('city',inplace=True)
