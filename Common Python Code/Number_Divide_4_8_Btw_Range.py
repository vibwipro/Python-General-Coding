'''
Python program with the given range between 4000 and 9000,
validate that each digit in the range is divisible by 4 and 8.
'''

div_by_4_8 = []

for d in range(4000, 9000):
    x = str(d)
    if (int(x[0]) % 4 == 0) and (int(x[1]) % 4 == 0) and (int(x[2]) % 4 == 0) and (int(x[3]) % 8 == 0):
        if (int(x[0]) % 8 == 0) and (int(x[1]) % 8 == 0) and (int(x[2]) % 8 == 0) and (int(x[3]) % 8 == 0):
            div_by_4_8.append(x)

print("Each digit of the numbers within range are divisible by 4 and 8 : ")
print(",".join(div_by_4_8))