n, m = map(int, input().split())
data = list(map(int, input().split()))

checked = [0] * 11

#무게 체크
for i in data:
    checked[i] += 1

print(checked)

result = 0

# 1~3
for i in range(1, m+1):
    n -= checked[i]
    result += checked[i] * n

print(result)