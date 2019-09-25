'''
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50.
H is 30.
D  is  the  variable  whose  values  should  be  input  to  your  program  in  a  comma-separated sequence.
Example:Let  us  assume  the  following  comma  separated  input  sequence  is  given  to  the program:
100,150,180
The output of the program should be:
18,22,24
'''

import math
no = input('Enter digits for which formula need to be calculated  : ')
no_digit = no.split(",")
c = 50
h = 30
no_output = []

for d in no_digit :
    print (d)
    q = math.floor(math.sqrt((2*c*int(d))/h))
    no_output.append(q)

print (no_output)