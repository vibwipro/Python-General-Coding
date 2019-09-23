'''
Write a program to find distancebetween two locations when their latitude and longitudes are given.
Hint: Use math module
'''

import math
p1 = input('Enter latitude and longitude of first point :')
pt1 = p1.split()
p2 = input('Enter latitude and longitude of second poit :')
pt2 = p2.split()
y = input('Do you want to calculate disctance between 2 points. Enter Y/N : ')

if (y.upper() == 'Y') :
    x = int(pt2[0]) - int(pt1[0])
    y = int(pt2[1]) - int(pt1[1])
    d = math.sqrt(x**2 + y**2)

    print ('Distance between 2 point are : ' + str(d))
else :
    print('Thank you for visiting. Given 2 points are ' + '(' + p1 + ') and (' + p2 + ')' )