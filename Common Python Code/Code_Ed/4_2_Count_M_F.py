'''
Find:
1. The number of men with a PhD
2. The number of women with a PhD
'''

import numpy as np
import pandas as pd

'''
ar = np.genfromtxt ('Data/4_SalaryGender', delimiter = ',', skip_header=1)
ar_g = list(zip(*ar))[1]
ar_c0, ar_c1 = ar_g.count(0), ar_g.count(1)
print ('Count of Male and femail is : ' + str(ar_c0) +' & ' + str(ar_c1))
'''

df = pd.read_csv('Data/4_SalaryGender', delimiter = ',')

#salary = np.array(df['Salary'])
gender = np.array(df['Gender'])
phd = np.array(df['PhD'])
#age = np.array(df['Age'])

men_count = 0
women_count = 0

for i in range(0, 100):
    if gender[i] == 1 and phd[i] == 1:
        men_count += 1
    if gender[i] == 0 and phd[i] == 1:
        women_count += 1

print('The number of men with a PhD is %i'%(men_count))
print('The number of women with a PhD is %i'%(women_count))
