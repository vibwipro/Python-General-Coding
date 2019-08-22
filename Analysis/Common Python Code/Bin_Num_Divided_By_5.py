'''
write a Python program that will accept binary numbers as an input form a user.
After the input, validate which binary numbers are divisible by 5 or not.

int() arguments
The Python int() method takes two arguments:

x – Number or string to be converted to integer object. Default argument is zero.
base – Base of the number in x. This can be 0 (code literal) or 2-36.
'''


binary_numbers = input("Please provide multiple sets of binary numbers that are comma separated: ")

numbers = [x for x in binary_numbers.split(',')]
binary_divisible_by_5 = []

for b in numbers:
    binary_int = int(b, 2)
    print (binary_int)
    if not binary_int % 5:
        binary_divisible_by_5.append(b)

print("The list of numbers that are divisible by 5: ")
print(','.join(binary_divisible_by_5))