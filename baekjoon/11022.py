import sys

t = int(input())
cnt = 1
while t > 0:
    a, b = map(int, input().split())
    print("Case #%d: %d + %d = %d" % (cnt, a, b, a+b))
    cnt += 1
    t -= 1

