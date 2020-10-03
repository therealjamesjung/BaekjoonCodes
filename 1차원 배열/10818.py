from sys import stdin

a = stdin.readline().rstrip()
l = stdin.readline().rstrip().split(' ')
l = [int(a) for a in l]
l.sort()
print(l[0], l[-1])
