from sys import stdin
import bisect, itertools

def is_prime(n):
    if n == 1:
        return False
    i=2
    while i*i<=n:
        if n%i == 0:
            return False
        i+=1
    return True

i = 2
l = [int(x) for x in range(10001)]

while i*i<=10001:
    if is_prime(i) is True:
        j = 2
        while i*j<=10001:
            try:
                l.pop(l.index(i*j))
            except:
                pass
            j+=1
    i+=1

n = int(stdin.readline().rstrip())

for i in range(n):
    a = int(stdin.readline().rstrip())
    p = l[2:bisect.bisect_left(l[2:], a)+2]

    tmp = []

    left = 0
    right = len(p)-1
    
    while True:
        if p[right]+p[left] == a:
            break
        elif p[right]+p[left] > a:
            right-=1
            left=0
        elif p[right]+p[left] < a:
            left+=1
    
    mid = int((left+right)/2)
    left = mid
    right = mid
    while True:
        if p[right]+p[left] == a:
            break
        elif p[right]+p[left] > a:
            left-=1
        elif p[right]+p[left] < a:
            right+=1
            left+=1

    print(p[left], p[right])

