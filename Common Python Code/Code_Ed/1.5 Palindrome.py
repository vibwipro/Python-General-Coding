'''
Design a code which will find the given number is Palindrome number or not.
Hint: Use built-in functions of string.

'''

print ('Enter a number to be checked for Palindrome : ')
ip = input()
a = ip
res = ''
for i in range (1, len(ip)+1):
    v = int(a) % 10
    res = res + '' + str(v)
    a = int(a) // 10

if (ip == res):
    print ('Input number ' + ip +  ' is a Palindrome')
else :
    print ('Input number ' + ip +  ' is not a Palindrome')