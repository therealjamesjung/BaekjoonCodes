from sys import stdin

a = stdin.readline().rstrip().split(' ')

try:
    c = int(float(a[0])/(int(a[2])-int(a[1])))
    print('-1') if c<0 else print(c+1)
except ZeroDivisionError:
    print('-1')