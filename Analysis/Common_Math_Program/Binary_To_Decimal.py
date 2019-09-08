import sys

def binary_to_decimal_conv (binary_string) :
    result = 0
    br_l = list(binary_string)
    j = len(br_l) - 1
    for i in range(0, (len(br_l)), 1):
        result += int(br_l[j]) * (2 ** i)
        print(str(br_l[j]) + ' ' + str (i))
        j = j -1
    return result



# Test
# Testing interface
i = 0
while True:
	if input("\n[{}] Exit(press e) or Continue(press c): ".format(i)).strip().lower() == "c":
		print("Decimal form: " + str(binary_to_decimal_conv(input("\nBinary?: "))))
	else:
		print("\nHope you enjoyed!")
		sys.exit()
	i += 1

# Binary to decimal conversion
# See explaination: https://i.imgur.com/heAT0PB.gif   ,
# https://www.electronics-tutorials.ws/binary/bin_2.html