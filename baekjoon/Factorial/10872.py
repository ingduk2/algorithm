import sys

n = int(sys.stdin.readline())
result = 1
for i in range(n, 0, -1):
    result *= i
str = repr(result)
print(str)
count = 0
for i in range(len(str)-1, 0, -1):
    if str[i] == '0':
        count += 1
    else:
        break
print(count)
