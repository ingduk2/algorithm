import sys
a = input()
n = input()
length = len(n)
sum = 0
for i in range(length):
    sum += int(n[i])
print(sum)