from sys import stdin

n = int(stdin.readline().rstrip())

for i in range(n):
    tmp = stdin.readline().rstrip().split()
    print('Case #'+str(i+1)+': '+tmp[0]+' + '+tmp[1]+' = '+str(int(tmp[0])+int(tmp[1])))