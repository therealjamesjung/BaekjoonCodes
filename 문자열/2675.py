from sys import stdin

n = int(stdin.readline().rstrip())

for i in range(n):
    a = stdin.readline().rstrip().split(' ')
    
    for x in a[1]:
        print(x*int(a[0]),end="")
    print('')
