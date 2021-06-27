from collections import deque

n = int(input())

for i in range(n):
    m, n, k = map(int, input().split(' '))
    graph = [[0] * n for x in range(m)]
    l = list()

    for _ in range(k):
        x, y = map(int, input().split(' '))
        l.append([x, y])
        graph[x][y] = 1

    queue = deque([l[0]])
    visited = list()
    cnt = 0

    answer = list()

    while True:
        node = queue.popleft()
        visited.append(node)
        l.remove(node)
        cnt += 1
        flag = 0

        for case in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if node[0] + case[0] < 0 or node[1] + case[1] < 0 or node[0] + case[0] >= m or node[1] + case[1] >= n:
                continue
            else:
                if graph[node[0] + case[0]][node[1] + case[1]] != 0 \
                        and [node[0] + case[0], node[1] + case[1]] not in visited \
                        and [node[0] + case[0], node[1] + case[1]] not in queue:
                    queue.append([node[0] + case[0], node[1] + case[1]])

                    flag = 1

        if len(l) == 0:
            answer.append(cnt)
            break

        if len(queue) == 0:
            answer.append(cnt)
            cnt = 0
            queue.append(l[0])

    print(len(answer))
