from sys import stdin
a = stdin.readline().rstrip().split(' ')

print(max(int(a[0][::-1]), int(a[1][::-1])))
