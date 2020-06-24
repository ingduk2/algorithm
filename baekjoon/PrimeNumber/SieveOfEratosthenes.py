p = [0 for i in range(100)]
pn = 0
c = [0 for i in range(101)]
n = 100
for i in range(2, n+1, 1):
    if not c[i]:
        p[pn] = i
        pn += 1
        for j in range(i*2, n+1, i):
            c[j] = True

print(p)
print(c)
