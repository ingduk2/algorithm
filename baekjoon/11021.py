import sys

t = int(input())
count = 1
while t > 0:
    a, b = map(int, input().split())
    print('Case #' + str(count) + ': ' + str(a + b))
    # print("Case #%d: %d" % (i + 1, A + B))
    count += 1
    t -= 1
