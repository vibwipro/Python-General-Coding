'''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in acomma-separated sequence on a single line
'''

no = input('Enter 2 (2000, 3200) digit between which numbers are find, which are divisible by 7 but are not a multiple of 5 : ')
no_digit = no.split()
no_new = []
cnt = 0
print (int(no_digit[0]))
print ( int(no_digit[1]))
for i in range (int(no_digit[0]), int(no_digit[1]) + 1) :

    if (i % 7 == 0 and i % 5 != 0) :
        no_new.append(i)

print (no_new)