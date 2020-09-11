import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))


print(n, m, arr)
start = 0
end = max(arr)

maxrice = max(arr)
result = 0
while start <= end:
    sum = 0
    mid = (start + end) // 2
    for j in arr:
        print(j, mid)
        if j > mid:
            sum += j - mid

    if sum < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

    print("==============", sum)
print(result)





