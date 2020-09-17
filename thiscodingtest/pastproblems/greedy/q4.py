# n = 5
# 3, 2, 1, 1, 9
# 만들 수 없는 양의 정수 금액 중 최소값 8

# n = 3
# 3 5 7
# 만들수 없는 최소값 1

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

target = 1
for i in arr:
    print(target)
    if target < i:
        break
    target += i

print(target)
