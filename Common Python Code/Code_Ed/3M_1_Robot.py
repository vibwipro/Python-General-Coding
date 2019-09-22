'''
A Robot moves in a Plane starting from the origin point (0,0). T
he robot can move toward UP, DOWN, LEFT, RIGHT. The trace of Robot movement is as given following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after directions are steps.
Write a program to compute the distance current position after sequence of movements.Hint: Use math module
'''

import math
up = input('Enter number of space robot moves up :')
dw = input('Enter number of space robot moves down :')
rt = input('Enter number of space robot moves right :')
lf = input('Enter number of space robot moves left :')


x = int(up) - int(dw)
y = int(rt) - int(lf)

d = math.sqrt(x**2 + y**2)

print('New position of robot is : (' + str(x) + ',' + str(y) + ')')

print ('Distance of robot from original starting point : ' + str(d))