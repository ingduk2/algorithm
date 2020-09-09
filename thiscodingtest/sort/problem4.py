n, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort(reverse=True)
print(arr1)
print(arr2)

for i in range(k):
    if arr1[i] < arr2[i]:
        arr1[i], arr2[i] = arr2[i], arr1[i]
    else:
        break

print(arr1)
print(arr2)
print(sum(arr1))