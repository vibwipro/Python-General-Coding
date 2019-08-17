def squared(n):
	return n * n

def cubed(n):
	return n * n * n

def raise_power(n, power):
    total = 1
    for t in range (power) :
        total = total * n
    return  total


def is_divisible(n, t):
	return n % t == 0

def is_even(n):
	return n % 2 == 0

def is_odd(n):
	return n % 2 != 0


print(list(map(squared, [1, 3, 5, 7, 9, 11, 13, 15])))
print(list(map( lambda x: raise_power (x,3), [1, 2, 5, 7, 9, 11, 13, 15])))

# for functions with multiple args
# see: https://www.quora.com/How-do-I-put-multiple-arguments-into-a-map-function-in-Python