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

a = int(stdin.readline().rstrip())
b = int(stdin.readline().rstrip())

l = []
for i in range(a,b+1):
    if is_prime(i) is True:
        l.append(i)
if len(l) == 0:
    print('-1')
else:
    print(sum(l))
    print(min(l))
