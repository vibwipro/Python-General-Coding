
def enum(ar):
	for index in range(len(ar)):
		yield((index, ar[index]))

# Test
case_1 = [19, 17, 20, 23, 27, 15]
for tup in list(enum(case_1)):
	print(tup)