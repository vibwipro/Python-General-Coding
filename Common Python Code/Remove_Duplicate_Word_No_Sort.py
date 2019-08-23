def duplicate_removal(w):
    word_list = []
    [word_list.append(s) for s in w if s not in word_list]
    return word_list


print("Input a few random words or sentences with some words as duplicates: ")
s = input()

print(" ".join(duplicate_removal(s.split())))