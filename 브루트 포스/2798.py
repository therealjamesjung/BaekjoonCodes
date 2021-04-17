from itertools import combinations
from bisect import bisect
from sys import stdin


a = stdin.readline().rstrip().split(' ')
b = stdin.readline().rstrip().split(' ')

b = [int(b) for b in b]

combination = combinations(b, 3)

s = []

for x in combination:
    s.append(sum(x))

s.sort()
print(s[bisect(s, int(a[1])) - 1])
