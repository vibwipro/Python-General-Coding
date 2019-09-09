'''
Write a program which will find factors of given number and find whether the factor is even or odd.
Hint: Use Loop with if-else statements
'''


print('Input number for which factor need to be identified : ')
n = input()

if ( int(n) % 2 == 0 ) :
    print ('Given number ' + n + ' is even factors')
else :
    print ('Given number ' + n + ' is odd Factors')

print ('Factorial of given number ' + n + ' is :' )
for i in range (1, int(n)+1) :
    if not ( int(n) % int(i)) :
        print (i)










