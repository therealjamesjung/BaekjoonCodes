from sys import stdin

def x(n):
    if n==1:
        return 1
    return x(n-1)*n

n = int(stdin.readline())
if n == 0:
    print(1)
else:
    print(x(n))