from sys import stdin

n = stdin.readline().rstrip().upper()

x = list(set([a for a in n]))

l = []

for a in x:
    l.append(n.count(a))

if l.count(max(l)) > 1:
    print('?')
else:
    print(x[l.index(max(l))])
