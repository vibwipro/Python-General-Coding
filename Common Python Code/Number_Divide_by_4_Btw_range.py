'''
write a Python program that’s given the range of numbers between 4000 and 9000 to validate that
each digit in the range is divisible by 4.
'''
div_by_4 = []

for d in range(4000, 9000):
    x = str(d)
    if (int(x[0] ) % 4 ==0) and (int(x[1] ) % 4==0) and (int(x[2] ) % 4==0) and (int(x[3] ) % 4==0):
        div_by_4.append(x)

print("Each digit of the numbers within range are divisible by 4 : ")
#print (div_by_4)
#### Remove quotes and Sqr bracket
print(",".join(div_by_4))