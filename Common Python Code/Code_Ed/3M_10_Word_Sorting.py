'''
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''

wd = input('Enter comma separated sequence of words that need to be sorted : ')
wd_s = wd.split(",")

wd_lst = list(wd_s)
wd_lst.sort()

print(wd_lst)