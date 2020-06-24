import math
a, b = map(int, input().split())

p = [0 for i in range(10000000)]
pn = 0
c = [False for i in range(1000001)]
n = b
c[0] = True
c[1] = True
for i in range(2, int(math.sqrt(n)) + 1, 1):
    if not c[i]:
        p[pn] = i
        pn += 1
        for j in range(i+i, n+1, i):
            c[j] = True

# for i in p:
#     if a < i < b:
#         print(i)

count = 0
for i in range(a, b + 1, 1):
    if not c[i]:
        print(i)