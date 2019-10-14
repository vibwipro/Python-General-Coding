'''
Write  a  program  that  accepts  a  sentence  and  calculate  the  number  of  upper  case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

ip = input('Enter a sentence fow which upper and lower case letter need to be counted : ')
a,b,c = 0,0,0
for i in ip :
    if (97 <= ord(i) <= 122) :
        a += 1
    if (65 <= ord(i) <= 90) :
        b += 1
    if (ord(i) == 32) :
        c += 1

print ('UPPER CASE ' + str(b))
print ('LOWER CASE ' + str(a))