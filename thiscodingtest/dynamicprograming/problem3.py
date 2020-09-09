n = int(input())

d = [0] * 101
arr = list(map(int, input().split()))

d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(n):
    d[i] = max(d[i-1], d[i-2] + arr[i])

print(arr[n-1])