import sys


def tile(n):
    if n == 1:
        return n
    else:
        if d[n] > 0:
            return d[n]
        d[n] = tile(n-1) + tile(n-2)
        return d[n] % 10007


sys.setrecursionlimit(2000)
n = int(sys.stdin.readline())
d = [0 for i in range(1000+1)]
d[1] = 1
d[2] = 2
print(tile(n))
