import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for tc in range(int(input())):
    n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

#init
distance = [[INF] * n for _ in range(n)]

x, y = 0, 0
q = [(graph[x][y], x, y)]
distance[x][y] = graph[x][y]

while q:
    # 최단거리 꺼내기
    dist, x, y = heapq.heappop(q)
    # 처리되었다면 무시
    if distance[x][y] < dist:
        continue
    # 인접 노드 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #범위 체크
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        cost = dist + graph[nx][ny]
        #현재 노드 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
        if cost < distance[nx][ny]:
            distance[nx][ny] = cost
            heapq.heappush(q, (cost, nx, ny))

print(distance[n - 1][n - 1])