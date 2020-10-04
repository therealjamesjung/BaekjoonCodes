from sys import stdin

n = int(stdin.readline().rstrip())

for i in range(n):
    a = stdin.readline().rstrip().split(' ')
    a = [float(x) for x in a]

    mean = (sum(a) - a[0])/a[0]
    cnt = 0

    for score in a[1:]:
        if score > mean:
            cnt += 1
    print('%.3f'%(round(cnt/a[0]*100, 3))+'%')
