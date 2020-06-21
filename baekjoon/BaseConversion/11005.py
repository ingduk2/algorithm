import sys

n, b = map(int, input().split())
results = []
mok = n
while mok != 0:
    nam = mok % b
    mok = int(mok / b)
    results.append(nam)

for i in range(len(results)-1, -1, -1):
    if results[i] > 9:
        results[i] = chr(results[i]+55)
    print(results[i], end='')
print()
