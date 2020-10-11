from sys import stdin

while True:
    a = [int(x) for x in stdin.readline().rstrip().split(' ')]

    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        break

    x = a[0]*a[0]
    y = a[1]*a[1]
    z = a[2]*a[2]

    if x+y == z or x+z == y or y+z == x:
        print('right')
    else:
        print('wrong')