'''
Write a program, whichwill find all the numbers between 1000 and 3000 (both included) such that each digit of a number is an even number. The numbers obtained should be printed in a comma separated sequence on a single line.Hint: In case of input data being supplied to the question, it should be assumed to be a console input.
Divide each digit with 2 and verify is it even or not.
'''

print('Enter 2 digit number between which even no is found : ')
a1 = input()
a1_digit = a1.split()

a = int(a1_digit[0])
b = int(a1_digit[1])
x = ''
for i in range (a, b+1) :
    c = i
    for j in range (0, 4) :
        if (c != 0) :
            v = int(c) % 10

            c = c // 10
            w = v % 2
            x = x + '' + str(w)

    #print(x)
    if (x == '0000') :
        print(str(i))
    else :
        x = ''



