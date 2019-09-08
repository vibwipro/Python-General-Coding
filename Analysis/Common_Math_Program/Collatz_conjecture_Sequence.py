import sys


# Collatz conjecture
# if n is even n // 2 is the next number
# else n * 3
# always reach 1.

# Collatz series generator
def collatz_conjecture(n):
    if n < 1:
        raise Exception("\n  Expected a value greater than 1")

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n


# If n will be negative then
# sequence will be infinite

i = 0
while True:
    if input("\n[%i] Do you want to Continue[Y/n]?: " % i).strip().lower() == "y":
        for v in collatz_conjecture(int(input("Enter Number?: "))):
            print("  => " + str(v))
        i += 1
    else:
        print("\nThank you !")
        sys.exit(0)

# See: https://en.wikipedia.org/wiki/Collatz_conjecture