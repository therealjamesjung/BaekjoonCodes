from sys import stdin

n = int(stdin.readline().rstrip())

for i in range(n):
    a = [int(x) for x in stdin.readline().rstrip().split(' ')]

    x = a[2]%a[0]
    y = (a[2]//a[0])+1

    if x==0:
        x = a[0]
        y -= 1

    print(str(x)+'%02d'%y)