from sys import stdin
from collections import Counter

a=[]

for i in range(3):
    a.append([int(x) for x in stdin.readline().rstrip().split(' ')])

a = list(map(list, zip(*a)))
print(Counter(a[0]).most_common()[-1][0], Counter(a[1]).most_common()[-1][0])