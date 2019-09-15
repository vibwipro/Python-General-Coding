'''
Please write a program which count and print the numbers of each character in a string input by console.
Example: If the following string is given as input to the program:abcdefgabc
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1
'''

print('Enter chnaracter for which counting need to be done : ')
ip = input()

ip_set = set(list(ip))
ip_len = len(ip_set)
count = 0
for i in ip_set :
    for j in ip :
        if (i == j) :
            count += 1
    print (i + ',' + str(count))
    count = 0
