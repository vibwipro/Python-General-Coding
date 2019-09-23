'''
Design a software for bank system. There should be options like cash withdraw, cash credit and change password.
According to user input, the software should provide required output.
Hint: Use if else statements and functions
'''

print ('Welcome to banking software system !')

print('Enter 1 for Cash Widrawl :')
print('Enter 2 for Cash Credit : ')
print('Enter 3 for change password :')
y = input()
if (y == '1') :
    Am = input ('Please enter amout you wnated to widraw : ')
    print ('Please collect your cash for Rs ' + Am + 'from widrawl box and recipt.')
    print ('Thank you for visiting.')
elif (y == '2') :
    Am = input ('Please enter amout you wnated to deposit : ')
    print ('Please keep cash in widrawl box.')
    print ('\n Your money for Rs ' + Am + ' is crdited to your bank account. \n\n Please collect your recipt. \n Thank you for visiting')
elif (y == '3'):
    pw = input ('Please enter new 4 digit password. : ')
    pw1 = input ('Re-enter 4 digit password. : ' )
    if (pw == pw1) :
        print ('Your password chnaged. \n Thank you for visiting.')
    else :
        print ('You have entered worng password.\n Thank you for visiting.')
else   :
    print('You have enterted a incorrect option.\nThank you for visiting.')