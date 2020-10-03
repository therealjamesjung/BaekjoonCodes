from sys import stdin

a = int(stdin.readline().rstrip())
b = int(stdin.readline().rstrip())
c = int(stdin.readline().rstrip())
n = [int(a) for a in str(a*b*c)]

for i in range(10):
    print(n.count(i))
