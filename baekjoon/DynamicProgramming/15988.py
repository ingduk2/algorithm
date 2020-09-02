import sys

t = int(sys.stdin.readline())

while t > 0:
    a = 1
    b = 2
    c = 4
    ret = 0
    n = int(sys.stdin.readline())
    for i in range(4, n + 1):
        # print(a, b, c, ret)
        ret = c + b + a
        a = b % 1000000009
        b = c % 1000000009
        c = ret % 1000000009
    if n == 1:
        print(a)
    if n == 2:
        print(b)
    if n == 3:
        print(c)
    if n > 3:
        print(ret % 1000000009)
    t -= 1

