import statistics
from statistics import mode


def most_frequent(List):
    counter = 0
    num = []

    for j in range (0,2):
        counter = 0
        for i in List:
            if i not in num :
                curr_frequency = List.count(i)
                if (curr_frequency > counter):
                    counter = curr_frequency
                    num.append(i)

    return num


List = [2, 2, 2, 3, 1, 3, 4, 4, 6, 6, 6, 4, 5, 5, 5]
print(most_frequent(List))