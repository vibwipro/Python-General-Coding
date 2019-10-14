'''
Give example of fsum and sum function of math library
'''

import math

no = input('Enter some numbers : ')
no_l = no.split()
no_lt =[]
for i in no_l :
    no_lt.append(int(i))


print(math.fsum(no_lt))

print(sum(no_lt))


