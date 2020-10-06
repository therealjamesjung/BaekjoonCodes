from sys import stdin
from math import sqrt

n = int(stdin.readline().rstrip())

a = int((sqrt(8*n + 1) - 1)/2 - 1e-8)
b = int(n - a*(a+1)/2)

if a == 0:
    print('1/1')
else:
    if a%2==0:
        print(str(a+2-b)+'/'+str(b))
    else:
        print(str(b)+'/'+str(a+2-b))
