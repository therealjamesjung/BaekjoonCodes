from sys import stdin

def is_prime(n):
    if n == 1:
        return False
    i=2
    while i*i<=n:
        if n%i == 0:
            return False
        i+=1
    return True


a = [int(x) for x in stdin.read().splitlines()]

i = 2
m = max(a)*2+1
l = [True]*m

while i*i<=m:
    if is_prime(i) is True:
        j = 2
        while i*j<=m:
            try:
                l[i*j] = False    
            except:
                pass
            j+=1
    i+=1

l[0] = False
l[1] = False

for x in a:
    if x is not 0:
        print(l[x+1:2*x+1].count(True))

