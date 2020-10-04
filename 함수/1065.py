from sys import stdin

n = int(stdin.readline().rstrip())
cnt=0

for a in range(n+1)[1:]:

    a = str(a)
    if len(a) == 1:
        cnt += 1
        continue
    
    d = int(a[1])- int(a[0])
    f= False

    for i in range(len(a)-1):
        if int(a[i+1]) - int(a[i]) == d:
            pass
        else:
            f = True
    if f is False:
        cnt += 1

print(cnt)
