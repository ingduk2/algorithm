n = int(input())
board = [[0] * (n + 1) for _ in range(n+1)]


k = int(input())

#apple
for i in range(k):
    x, y = map(int, input().split())
    board[x][y] = 2


l = int(input())
goinfo = []
for i in range(l):
    t, c = input().split()
    goinfo.append((int(t), c))

#    동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def check(x, y):
    if 0 < x <= n and 0 < y <= n and board[x][y] != 1:
        return True
    return False

x = 1
y = 1
time = 0

# 1 은 지렁이 , 2 는 사과 , 0은 길
direction = 0
board[x][y] = 1
q = [(x, y)]
while True:

    prevx = x
    prevy = y

    # 방향 전환. 기본은 y++
    for i in goinfo:
        t, c = i
        if t == time:
            direction = turn(direction, c)

    x += dx[direction]
    y += dy[direction]
    time += 1

    if check(x, y):
        if board[x][y] == 0:
            board[x][y] = 1
            q.append((x, y))
            px, py = q.pop(0)
            board[px][py] = 0
        if board[x][y] == 2:
            board[x][y] = 1
            q.append((x, y))
    else:
        break


print(time)



# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D
