'''
Store the “Age” and “PhD” columns in one DataFrame and delete the data of all people
who don’t have a PhD from SalaryGender CSV file
'''

import numpy as np
import pandas as pd

df = pd.read_csv('Data/4_SalaryGender', delimiter = ',')

salary = np.array(df['Salary'])
gender = np.array(df['Gender'])
phd = np.array(df['PhD'])
age = np.array(df['Age'])


data = {}
for i in range (0, 100):
    if (phd[i] == 1) :
        data = pd.DataFrame(age, phd)
    else :
        pass

print(data)
