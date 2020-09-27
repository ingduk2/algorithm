n, m = map(int, input().split())
arr = []
temp = [[0] * m for _ in range(n)]

for i in range(n):
    arr.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# dfs
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx <n and 0<= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


def dfs(count):
    global result

    #벽 3개
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = arr[i][j]

        #바이러스 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return
    #빈 공간에 울타리 설치.
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                count +=1
                dfs(count)
                arr[i][j] = 0
                count -=1

dfs(0)
print(result)