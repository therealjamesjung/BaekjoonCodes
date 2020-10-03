from sys import stdin

n = int(stdin.readline().rstrip())

for i in range(n):
    tmp = stdin.readline().rstrip().split()
    print(int(tmp[0])+int(tmp[1]))
    