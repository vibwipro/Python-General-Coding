'''
Write a program that accepts a sequence of whitespace separated words as input and   prints   the   words   after   removing   all   duplicate   words   and   sorting   them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''

wd = input('Enter comma separated sequence of words that need to be sorted : ')
wd_s = wd.split()

wd_lst = list(wd_s)
wd_lst.sort()
wd_fln = ''
wd_lst1 = []

for i in wd_lst :
    if i not in wd_lst1 :
        wd_lst1.append(i)
        wd_fln = wd_fln + i + ' '


print(wd_fln)