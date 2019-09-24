'''
Write a program which can compute the factorial of a given numbers. Use recursion to find it.
Hint: Suppose the following input is supplied to the program:8
Then, the output should be:40320
'''

def fact (x):
    if (x == 0):
        return (1)
    else :
        return (x * fact(x-1))


n = input('Enter no for which factorial need to be find : ')
y = fact(int(n))
print ('Factorial of number ' + str(n) + ' is : ' + str(y))