'''
Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.
Hint: In case of input data being supplied to the question, it should be assumed to be a console input.
'''

print('Input number word for : ')
n = input()
mp = list(map(lambda x: ord(x), n))
mp.sort()
mc = list(map(lambda y: chr(y), mp))
dd = ''
for z in mc :
    dd = dd + z

print(dd)


