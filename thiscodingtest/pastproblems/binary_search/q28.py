def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid -1)
    else:
        return binary_search(array, mid + 1, end)



n = int(input())
data = list(map(int, input().split()))

idx = binary_search(data, 0, n-1)

if idx == None:
    print(-1)
else:
    print(idx)


