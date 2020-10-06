from sys import stdin

l= [[1 for a in range(15)] for x in range(15)]
l[0] = [x+1 for x in range(15)]

for i in range(1, 15):
    for j in range(1, 15):
        l[i][j] = l[i][j-1] + l[i-1][j]

n = int(stdin.readline().rstrip())

for i in range(n):
    a = int(stdin.readline().rstrip())
    b = int(stdin.readline().rstrip())

    print(l[a][b-1])