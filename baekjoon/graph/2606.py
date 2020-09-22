n = int(input())
m = int(input())
visited = [False] * (n + 1)

graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)



dfs(graph, 1, visited)
print(visited)
result = 0
for i in visited:
    if i:
        result += 1
print(result - 1)

