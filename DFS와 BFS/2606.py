from collections import deque

n = int(input())
v = int(input())

graph = dict()

for i in range(n):
    graph[i + 1] = list()

for i in range(v):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

for a in graph.values():
    a.sort()

visited = list()
queue = deque([1])
cnt = 0

while queue:
    node = queue.popleft()
    visited.append(node)
    cnt += 1

    for i in graph[node]:
        if i not in queue and i not in visited:
            queue.append(i)

print(cnt - 1)
