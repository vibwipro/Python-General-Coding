'''
write a Python program that will accept a variation of words or numbers that are whitespace separated.
After the user has provided the input, remove all duplicate words, sort the words and numbers,
and print the input.
'''

s = input("Input a few random words or sentences with some words as duplicates: ")

words = [word for word in s.split(" ")]

print("Input before duplication removal and sorting: ")
print(s)
print("\nInput after duplication removal and sorting: ")
print(" ".join(sorted(list(set(words)))))
