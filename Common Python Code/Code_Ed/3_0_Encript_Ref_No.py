'''
Key issuesBuild a system where when user enters Reference ID it is encrypted,
so that hackers cannot view the mapping of Reference ID and finger print
'''

print('Enter your 12 digit refference number (alphabet & number) which need to be encrypted : ')
n = input()
ip = 0
for i in range (1, 4) :
    if (len(n) != 12) :
        print('Refference number entered is not correct')
        print('Enter your 12 digit refference number which need to be encrypted : ')
        n = input()
        ip += 1
        if (ip == 3) :
            print ('You have exceded maximum number of request, try again after some time.')
            exit()
    else :
        break
fl = ''
for j in n :
    if (j.isalpha()) :
        ak = int(ord(j)) + 20
        fl = fl + chr(ak)
    else :
        ak = int(ord(j)) - 15
        fl = fl + chr(ak)


print (fl)

print('Do you want reference number to be decrupted ?')
print('Enter Y or N')
de = input()
f2 =''
if (de.upper() == 'Y') :
    print('Enter 12 digit encripted reference number : ')
    en = input()
    for x in en :
        if (ord(x) <= 42) :
            bk = ord(x) + 15
            f2 = f2 + chr(bk)
        else :
            bk = ord(x) - 20
            f2 = f2 + chr(bk)
else :
    exit()

print(f2)