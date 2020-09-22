import sys
sys.setrecursionlimit(10**8)

t = int(sys.stdin.readline().rstrip())


dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

def search(array, x, y):

    #범위체크
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if array[x][y] == 1:
        array[x][y] = 0

        search(array, x-1, y)
        search(array, x, y+1)
        search(array, x, y-1)
        search(array, x+1, y)
        return True
    return False

while t > 0:
    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    array = [[0] * m for _ in range(n)]

    #x, y input
    for i in range(k):
        y, x = map(int, sys.stdin.readline().rstrip().split())
        array[x][y] = 1

    result = 0
    for i in range(m): #가로
        for j in range(n): #세로
            if search(array, j, i) == True:
                result += 1

    print(result)

    t -= 1


