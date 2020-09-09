n, m = map(int, input().split())


money = []
for i in range(n):
    money.append(int(input()))


print(n, m, money)


d = [10001] * (m + 1)
d[0] = 0


for j in money:
    for i in range(j, m + 1):
        d[i] = min(d[i], d[i-j] + 1)

print(d)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])

