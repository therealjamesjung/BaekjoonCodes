from sys import stdin

a = [int(x) for x in stdin.readline().rstrip().split(' ')]
if a[0] >= a[2]:
    print(1)
else:
    if (a[2]-a[0])%(a[0]-a[1])==0:
        print(int((a[2]-a[0])/(a[0]-a[1])+1))
    else:
        print(int((a[2]-a[0])/(a[0]-a[1])+2))