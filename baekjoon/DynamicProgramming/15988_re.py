import sys


t = int(sys.stdin.readline())
d = [0 for i in range(1000000 + 1)]
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 1000000 + 1):
    d[i - 1] = d[i - 1] % 1000000009
    d[i - 2] = d[i - 2] % 1000000009
    d[i - 3] = d[i - 3] % 1000000009
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]

while t > 0:
    n = int(sys.stdin.readline())
    print(d[n] % 1000000009)
    t -= 1
