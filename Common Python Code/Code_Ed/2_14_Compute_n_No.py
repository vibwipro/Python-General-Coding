'''
Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0).
Example:If the following n is given as
input to the program:5
Then, the output of the program
should be:3.55
'''

print ('Enter no for which following computing is required  1/2+2/3+3/4+...+n/n+1 : ')
n = input()
m = int(n)
total = 0
for i in range (1, m + 1) :

    total = total + (i/(i+1))


print (total)