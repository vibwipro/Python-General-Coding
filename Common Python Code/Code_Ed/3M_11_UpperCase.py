'''
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following inputis supplied to the program:
Hello worldPractice makes perfect
Then, the output should be:
HELLO WORLDPRACTICE MAKES PERFECT
'''
print ('Enter data which need to be converted to upper case : ')
lines = []
while True :
    line = input()
    if line:
        lines.append(line)
    else :
        break
text = '\n'.join(lines)

print (text.upper())