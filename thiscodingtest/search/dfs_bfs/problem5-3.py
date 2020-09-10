n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph[0])
print(graph[1])
print(graph[2])
print(graph[3])


def dfs(x, y):
    # print("============")
    # print(graph[0])
    # print(graph[1])
    # print(graph[2])
    # print(graph[3])
    # print("============")

    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        print("success")
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            print(i, j, "=-=-=-=-=-=-=-=-=-=")
            print("============")
            print(graph[0])
            print(graph[1])
            print(graph[2])
            print(graph[3])
            print("============")
            result += 1

print(result)

# 4 5
# 00110
# 00011
# 11111
# 00000
