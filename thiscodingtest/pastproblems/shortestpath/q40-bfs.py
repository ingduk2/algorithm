from collections import deque

def bfs(graph, start, visited):
    queue = deque()
    queue.append([start, 0])
    visited[start] = True
    distance[start] = 0
    while queue:
        v, dist = queue.popleft()
        for i in graph[v]:
            if not visited[i[0]]:
                cost = dist + i[1]
                queue.append([i[0], i[1]])
                distance[i[0]] = cost
                visited[i[0]] = True

INF = int(1e9)
n, m = map(int, input().split())
start = 1
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

print(graph)

visited = [False] * 9
bfs(graph, 1, visited)
print(distance)

result = []
max_distance = 0
max_node = 0
for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)
print(max_node, max_distance, len(result))