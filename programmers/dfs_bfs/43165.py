def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, computers):
    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    graph = []
    for i, com in enumerate(computers):
        for j, node in enumerate(com):
            if node == 1 and i != j:
                graph.append([i + 1, j + 1])

    graph = sorted(graph, key=lambda x : x[0])
    for a, b in graph:
        union_parent(parent, a, b)

    node_set = set()
    for i in range(1, n + 1):
        node_set.add(find_parent(parent, i))

    return len(node_set)


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))

n = 4
computers = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]
print(solution(n, computers))