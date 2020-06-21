import sys

word = input()
length = len(word)
startPoint = 0
while startPoint < length:
    print(word[startPoint: startPoint+10])
    startPoint += 10
