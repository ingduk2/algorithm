import sys


t = int(sys.stdin.readline())
d = [0 for i in range(10 + 1)]
d[1] = 1
d[2] = 2
d[3] = 4
while t > 0:
    n = int(sys.stdin.readline())
    for i in range(4, n + 1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    print(d[n])
    t -= 1

