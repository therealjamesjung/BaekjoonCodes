from sys import stdin

while True:
    a = stdin.readline().rstrip().split(' ')
    if a[0] == '':
        break
    else:
        print(int(a[0])+int(a[1]))
