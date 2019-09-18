'''
Please  write  a  program  to  randomly  generate  a  list  with  5  numbers,  which  are divisible by 5 and 7 ,
between 1 and 1000 inclusive.
'''

print('Enter 2 digit number between which list is found : ')
no = input()
no_digit = no.split()
no_new = []
cnt = 0
print (int(no_digit[0]))
print ( int(no_digit[1]))
for i in range (int(no_digit[0]), int(no_digit[1]) + 1) :

    if (i % 35 == 0) :
        no_new.append(i)
        cnt += 1

        if (cnt == 5) :
            print(no_new)
            exit()


print (no_new)

