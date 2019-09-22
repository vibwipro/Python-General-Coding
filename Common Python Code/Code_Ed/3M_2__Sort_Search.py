'''
Data of XYZ company is stored in sorted list.
Write a program for searching specific data from that list.
Hint: Use if/elif to deal with conditions
'''

import re
print ('Enter sorted list of lines : ')
lines = []
while True :
    line = input()
    if line:
        lines.append(line)
    else :
        break
text = '\n'.join(lines)

test_1 = text.split("\n")

sr = input('Enter data you wanted to search : ')
sr_spt = sr.split()
for i in sr_spt :
    for j in test_1 :

        if (i.strip() == j.strip()) :
            print ('Character found in the list is : ' + i)
            break

print('Character not found in the list is : ' + i)



