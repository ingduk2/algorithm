# 왼쪽부터
# 가보지 않았다면 회전한 다음 왼쪽으로 한칸 전진
# 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 경우 방향 유지, 한칸 뒤로 가고 1단계로 돌아간다.

n, m = map(int, input().split())
a, b, d = map(int, input().split())

dMap = [[0] * m for _ in range(n)]
dMap[a][b] = 1


moveArr = [
    (-1, 0),  # 0
    (0, 1),  # 1
    (1, 0),   #2
    (0, -1),   #3
]

mapArr = []
for i in range(n):
    mapArr.append(list(map(int, input().split())))

print(n, m)
print(a, b, d)
print(mapArr)


def moving(movex, movey):
    dx = a + movex
    dy = b + movey


    if mapArr[dx][dy] == 0 and dMap[dx][dy] == 0:
        print("==moving ", dx, dy, mapArr[dx][dy])
        return True

    return False

nomovecount = 0
result = 1
while True:
    # 1 left
    d -= 1
    if d < 0:
        d = 3

    # 2 is possible Move
    print(moveArr[d][0], moveArr[d][1])
    if moving(moveArr[d][0], moveArr[d][1]):
        print("possible")
        a += moveArr[d][0]
        b += moveArr[d][1]
        dMap[a][b] = 1
        result += 1
        nomovecount = 0
    else:
        print("fail")
        nomovecount += 1

    # 3
    if nomovecount == 4:
        print("full")
        # 방향 유지 한칸 뒤로
        if moving(moveArr[d][0] * -1, moveArr[d][1] * -1):
            a += moveArr[d][0] * -1
            b += moveArr[d][1] * -1
        else:
            break
        nomovecount = 0


print(dMap)
print(result)


# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1


