'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡-Y-1.

Example:
Suppose the following inputs are given to the program:3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''

import math
no = input('Enter 2 digits X,Y as input and generates a 2-dimensional array : ')
n = no.split(",")
m = 0
in_ar = []
ot_ar = []
x = 0
for i in range (0, int(n[0])) :
    for j in range (0, int(n[1])) :
        in_ar.append(m)
        m = m + x
        if ( j == int(n[1])-1) :
            m = 0
            break
    x += 1
    ot_ar.append(in_ar)
    in_ar = []
print (ot_ar)
