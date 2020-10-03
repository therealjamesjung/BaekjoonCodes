from sys import stdin

a = stdin.readline().rstrip().split(' ')
l = stdin.readline().rstrip().split(' ')

for data in l:
    if int(data) < int(a[1]):
        print(data, end=" ")