'''
Please   write   a   program   which accepts  a   string   from   console   and   print   the characters that have even indexes.
Example: If the following string is given as input to the program:H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:Helloworld
'''

print('Input string for which even index is printed : ')
ip = input()
res = ''
for i in range (0, len(ip), 2) :
    res = res + str(ip[i])

print (res)
