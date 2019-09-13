'''
Please write a program which accepts a string from console and print it in reverse order.
Example: If the following string is given as input to the program: rise to vote sir
Then, the output of the program should be:
ris etov ot esir
'''

print('Enter string which need to be reversed : ')
ip = input()
rec =''
for i in reversed (range( len(ip))) :
    rec = rec + ip[i]

print (rec)