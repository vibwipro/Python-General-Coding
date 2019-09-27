'''
Write  a  program  which  accepts  a  sequence  of  comma  separated  4  digit  binary numbers  as  its  input  and  then  check  whether  they  are  divisible  by  5  or  not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence
Example:
0100,0011,1010,1001
Then the output should be:
1010
'''

bno = input('Enter comma separated sequence of binary number that need checked for 5 : ')
bno_s = bno.split(",")

bno_lst = list(bno_s)

bno_fln = ''


for i in bno_lst :
    a = int(i,2)
    if (a % 5 == 0) :
        bno_fln = bno_fln + str(i) + ','


print(bno_fln)