import sys

n = int(sys.stdin.readline().rstrip())
store = list(map(int, sys.stdin.readline().rstrip().split()))
store.sort()
m = int(sys.stdin.readline().rstrip())
customer = list(map(int, sys.stdin.readline().rstrip().split()))

print(n)
print(store)
print(m)
print(customer)


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


for i in customer:
    if binary_search(store, i, 0, n - 1) is None:
        print("no")
    else:
        print("yes")



