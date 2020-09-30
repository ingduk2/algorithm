n = int(input())

data = list(map(int, input().split()))


prevsum = 1e9
result = 0
antena = 1
while antena <= max(data):
    sum = 0
    for i in data:
        sum += abs(i - antena)

    if prevsum > sum:
        prevsum = sum
        result = antena
    print(sum)
    antena += 1

print("===", result)

