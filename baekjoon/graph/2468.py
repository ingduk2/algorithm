import sys
sys.setrecursionlimit(10**8)

n = int(input())
array = []
min_num = 10000
max_num = 0
for i in range(n):
    a = list(map(int, input().split()))
    min_num = min(min_num, min(a))
    max_num = max(max_num, max(a))
    array.append(a)


def dfs(data, x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if data[x][y] == 0:
        data[x][y] = 1
        dfs(data, x, y+1)
        dfs(data, x, y-1)
        dfs(data, x+1, y)
        dfs(data, x-1, y)
        return True
    return False

# 1. 수위별로 다른 array 생성.
# 2. 0인것을 dfs 묶어서 영역수 세기
# 3. 최대인 영역수 고르기
result = 1
for i in range(min_num, max_num + 1):
    data = [[0] * n for i in range(n)]
    for x in range(n):
        for y in range(n):
            if array[x][y] <= i:
                data[x][y] = 1



    # 3.
    cnt = 0
    for dx in range(n):
        for dy in range(n):
            if dfs(data, dx, dy) == True:
                cnt += 1
    result = max(result, cnt)
print(result)