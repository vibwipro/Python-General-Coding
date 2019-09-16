'''
With a given list [12,24,35,24,88,120,155,88,120,155],
write a program to print this list after removing all duplicate values with original order reserved.
'''

a = [12,24,35,24,88,120,155,88,120,155]

b = []
c = []

for x in a :
    if x not in b :
        b.append(x)

for y in reversed(b) :
    c.append(y)

print (c)


# b = b + ' ' + str(a[j]) + ','