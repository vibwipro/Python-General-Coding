'''
Write a program that accepts a sentence and calculate the number of letters and digits.Suppose if the entered string is: Python0325
Then the output will be:LETTERS: 6DIGITS:4

Hint: Use built-in functions of string.
'''

print('Input string with number and char :')
ip = input()
c = 0
n = 0
for i in ip :

    if (i.isdigit()) :
        n = n + 1
    if (i.isalpha()) :
        c = c + 1

print ('Letter : ' + str(c))
print ('Number : ' + str(n))