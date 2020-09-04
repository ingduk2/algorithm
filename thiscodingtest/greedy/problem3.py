n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

print(arr)

result = 0

for sub in arr:
    result = max(result, min(sub))
print(result)
