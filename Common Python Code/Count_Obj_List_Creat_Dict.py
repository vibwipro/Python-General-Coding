from collections import Counter

x = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6]
data = []
for i in x :
    data.append(int(i))

print (data)
y  = Counter(data)

print (y)