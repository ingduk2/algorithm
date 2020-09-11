import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))


print(n, m, arr)

maxrice = max(arr)
while True:
    sum = 0
    for j in arr:
        print(j, maxrice)
        if j > maxrice:
            sum += j - maxrice

    if sum >= m:
        break
    print("==============", sum)
    maxrice -= 1
print(maxrice)


