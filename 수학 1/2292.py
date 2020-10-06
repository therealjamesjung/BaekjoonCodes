from sys import stdin

n = int(stdin.readline().rstrip())
c = 1

for i in range(n):
    d = 3*(i**2) + 3*i + 1
    if d>=n:
        print(i+1)
        break
    else:
        c = d