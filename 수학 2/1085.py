from sys import stdin

a = [int(x) for x in stdin.readline().rstrip().split(' ')]
print(min(a[3]-a[1],a[1],a[0],a[2]-a[0]))