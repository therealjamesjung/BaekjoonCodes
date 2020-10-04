from sys import stdin

l = set()

for i in range(10):
    a = stdin.readline().rstrip()
    l.add(int(a)%42)

print(len(l))