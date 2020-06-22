import sys
import math
import copy

MAX = 1000000
p = [0 for i in range(MAX)]
pn = 0
c = [False for i in range(MAX + 1)]
n = MAX
c[0] = True
c[1] = True
for i in range(2, MAX + 1, 1):
    if not c[i]:
        p[pn] = i
        pn += 1
        for j in range(i + i, n + 1, i):
            c[j] = True

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(pn):
        if not c[n - p[i]]:
            print("%d = %d + %d" % (n, p[i], n - p[i]))
            break
