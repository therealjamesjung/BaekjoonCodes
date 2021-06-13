import operator

n = int(input())

li = list()

for i in range(n):
    a = [int(x) for x in input().split(' ')]
    a.append(i)
    li.append(a)

li = sorted(li, key=operator.itemgetter(0, 1))[::-1]

rank = 1
cnt = 1

for i, data in enumerate(li):
    cnt = 1
    for j in li[:i]:
        if j[0] > data[0] and j[1] > data[1]:
            cnt += 1
    data.append(cnt)

li = sorted(li, key=operator.itemgetter(2))

print(' '.join(str(x[3]) for x in li))
