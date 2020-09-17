n, m = map(int, input().split())
arr = list(map(int, input().split()))

checked = []

def checkExist(a, b):
    #swap
    a, b = b, a
    for i in checked:
        x, y = i
        if x == a and y == b:
            return True
    return False


result = 0
for a in range(len(arr)):
    for b in range(len(arr)):
        if arr[a] != arr[b]:
            if not checkExist(a+1, b+1):
                checked.append((a+1, b+1))
                print(a+1, b+1)
                result += 1

print(result)
