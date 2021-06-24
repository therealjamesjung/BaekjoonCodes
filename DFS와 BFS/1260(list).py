from collections import deque

n, m, v = map(int, input().split(' '))


def dfs(graph, node, visited):
    if node in visited:
        return

    visited.append(node)
    print(node, end=' ')

    for n in graph[node]:
        dfs(graph, n, visited)


def bfs(graph, node, visited):
    queue = deque([node])
    while queue:
        node = queue.popleft()
        visited.append(node)
        print(node, end=' ')

        for n in graph[node]:
            if n not in queue and n not in visited:
                queue.append(n)


graph = dict()

for i in range(n):
    graph[i + 1] = list()

for i in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

for n in graph.values():
    n.sort()

stack = list()
dfs(graph, v, stack)

print('')
stack.clear()

bfs(graph, v, stack)
