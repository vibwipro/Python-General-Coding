'''
Extract data from the givenSalaryGender CSV fileand store the data from each column in a separate NumPy array
'''


import numpy as np

ar = np.genfromtxt ('Data/4_SalaryGender', delimiter = ',', skip_header=1)


print(ar)
