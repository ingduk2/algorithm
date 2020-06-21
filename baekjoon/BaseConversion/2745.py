import sys

n, b = input().split()
b = int(b)
chasu = len(n)-1
result = 0
for i in range(len(n)):
    if ord(n[i]) >= 65:
        num = ord(n[i]) - 55
    else:
        num = int(n[i])
    result += num * (b ** chasu)
    chasu -= 1
print(result)
