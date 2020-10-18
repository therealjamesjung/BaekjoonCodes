from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    a = [int(x) for x in stdin.readline().rstrip().split(' ')]
    
    d = ((a[3]-a[0])*(a[3]-a[0])+(a[4]-a[1])*(a[4]-a[1]))**0.5

    if a[2] == a[5]:
        if d == 0:
            print('-1')
        elif d > a[2]+a[5]:
            print('0')
        elif d < a[2]+a[5]:
            print('2')
        elif d == a[2]+a[5]:
            print('1')

    else:
        if d == 0:
            print('0')
            continue
            
        if a[2]>a[5]:
            r1 = a[2]
            r2 = a[5]
        else:
            r1 = a[5]
            r2 = a[2]

        if r1+r2 < d:
            print('0')
        elif r1+r2 == d:
            print('1')
        elif r1+r2 > d and r1-r2 < d:
            print('2')
        elif r1-r2 == d:
            print('1')
        elif r1-r2 > d:
            print('0')
