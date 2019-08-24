'''
write a Python program that will take the input of words (comma-separated format).
Once the user provides the words, sort and print the words in alphabetical order.

if the user inputs: tornado,hurricane,tsunami,flood,thunderstorm,hail,rain,wind
Then the output should be: flood,hail,hurricane,rain,thunderstorm,tornado,tsunami,wind
'''

words = input("Provide a list of words that are comma-separated: ")
words_split = [x for x in words.split(',')]
words_split.sort()
print("User input of words: ")
print(words)
print("User words sorted alphabetically: ")
print(','.join(words_split))