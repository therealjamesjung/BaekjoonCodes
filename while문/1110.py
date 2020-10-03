from sys import stdin

a = stdin.readline().rstrip()
t = int(a)
cnt=0

if int(a)<10:
    s = str(int(a)*10)

while True:
    cnt+=1
    if len(a) > 1:
        s = str(int(a[0])+int(a[1]))
    else:
        s = a[0]
    
    if len(s) > 1:
        if len(a) > 1:
            a = a[1]+s[1]
        else:
            a = a[0]+s[1]
    else:
        if len(a) > 1:
            a = a[1]+s[0]
        else:
            a = a[0]+s[0]


    if t == int(a):
        print(cnt)
        break
