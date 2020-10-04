from sys import stdin

n = int(stdin.readline().rstrip())
cnt=0

for x in range(n):
    a = stdin.readline().rstrip()
    l = []
    last = 0

    for i in range(len(a)-1):
        if a[i] != a[i+1]:
            l.append(a[last:i+1])
            last = i+1
            if i+1 == len(a)-1:
                l.append(a[i+1])
        else:
            if i+1 == len(a)-1:
                l.append(a[last:i+2])

    if len(l) == len(set(l)):
        if len(l) == len(set([x[0] for x in set(l)])):
            cnt += 1

print(cnt)
