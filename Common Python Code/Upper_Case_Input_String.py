'''
write a Python program that will accept a few sentences as input from a user and print the sentences in upper case
after user input.

'''

sentences = []

print("Please enter a few sentences: ")
s = input()

while True:
    if s:
        sentences.append(s.upper())
        break
    else:
        break


for sentence in sentences:
    print("Sentences after implementing the upper() function: ")
    print(sentence)
