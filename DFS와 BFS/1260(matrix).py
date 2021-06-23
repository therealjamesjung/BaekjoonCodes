from collections import deque


def dfs(graph, node, visited):
    if node in visited:
        return
    visited.append(node)
    print(node, end=" ")
    for i, a in enumerate(graph[node - 1]):
        if a != 0:
            dfs(graph, i + 1, visited)


"""
def bfs(graph, node, visited, queue):
    if node in visited:
        return
    visited.append(node)
    print(node, end=" ")
    for i, a in enumerate(graph[node - 1]):
        if a != 0 and i + 1 not in visited and i + 1 not in queue:
            queue.append(i + 1)
    if len(queue) != 0:
        bfs(graph, queue.popleft(), visited, queue)
"""


def bfs(graph, node, visited):
    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()
        visited.append(node)
        print(node, end=" ")
        for i, a in enumerate(graph[node - 1]):
            if a != 0 and i + 1 not in visited and i + 1 not in queue:
                queue.append(i + 1)


n, m, v = map(int, input().split(' '))

matrix = [[0] * n for x in range(n)]

for i in range(m):
    a, b = map(int, input().split(' '))
    matrix[a - 1][b - 1] = 1
    matrix[b - 1][a - 1] = 1

stack = list()
queue = deque()

dfs(matrix, v, stack)
stack.clear()
print('')
bfs(matrix, v, stack)
