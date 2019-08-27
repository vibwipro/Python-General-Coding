import pandas as pd

df = pd.read_csv("Data/stock_data.csv")
print(df)
print('#####################################################################')

######## skip header
df = pd.read_csv("Data/stock_data.csv", skiprows=1)
#print(df)

##### header work same as skiprows
df = pd.read_csv("Data/stock_data.csv", header=2) # skiprows and header are kind of same
#print (df)

####
df = pd.read_csv("Data/stock_data.csv", header=None, names = ["ticker_1","eps_1","revenue_1","people_1"])
###print(df)

###### Read only 2 records
df = pd.read_csv("Data/stock_data.csv",  nrows=2)
#print(df)


df = pd.read_csv("Data/stock_data.csv", na_values=["n.a.", "not available"])
#print(df)

import xlrd
########## Read from xls sheet
df = pd.read_excel("Data/stock_data.xlsx","Sheet1")
print(df)

import openpyxl
#### write to xls sheet
df.to_excel("Data/new.xlsx", sheet_name="stocks", index=False, startrow=2, startcol=1)