from sys import stdin
from math import sqrt

n = int(stdin.readline().rstrip())

for i in range(n):
    a = [int(x) for x in stdin.readline().rstrip().split(' ')]
    d = a[1]-a[0]

    x = int(sqrt(d))

    if x*x == d:
        print(2*x-1)
    elif x*x+x >= d:
        print(2*x)
    elif x*x+x < d:
        print(2*x+1)