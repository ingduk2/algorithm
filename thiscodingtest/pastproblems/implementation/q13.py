from itertools import combinations
n, m = map(int, input().split())

data = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        data[i+1][j+1] = a[j]

print(data)

# 0 은 공란, 1은 집 , 2는 치킨깁

def solution():
    home = []
    chicken = []
    for i in range(n+1):
        for j in range(n+1):
            if data[i][j] == 1:
                home.append((i, j))
            elif data[i][j] == 2:
                chicken.append((i, j))


    print(home)
    print(chicken)

    combinationlist = list(combinations(chicken, m))

    result = 1e9
    for combination in combinationlist:
        resultsum = 0
        ##최소값
        for h in home:
            temp = 1e9
            for c in combination:
                val = abs(h[0]-c[0]) + abs(h[1]-c[1])
                print(h, c , val)
                temp = min(temp, val)
            resultsum += temp
        result = min(result, resultsum)



    return result


print(solution())

# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2