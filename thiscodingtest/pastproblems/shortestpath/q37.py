# n = int(input())
# m = int(input())


import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

# start = int(input())

graph = [[] for i in range(n + 1)]


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))



def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    for i in range(1, n + 1):
        if distance[i] == INF:
            print("0" , end=' ')
        else:
            print(distance[i], end=' ')
    print()


for i in range(1, n + 1):
    dijkstra(i)


# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4



