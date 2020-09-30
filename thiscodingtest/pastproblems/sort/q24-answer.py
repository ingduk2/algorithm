#중간에 올 경우가 최소값이다.
n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n-1) // 2])
