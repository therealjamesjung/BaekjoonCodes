from sys import stdin

n = int(stdin.readline().rstrip())

for i in range(n):
    tmp = ' '*(n-i-1)+'*'*(i+1)
    print(tmp)