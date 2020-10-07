from sys import stdin

def is_prime(n):
    if n == 1:
        return False
    flag = True
    for i in range(n+1)[2:-1]:
        if n%i == 0:
            flag = False
            break

    return flag

n = int(stdin.readline().rstrip())
a = [int(x) for x in stdin.readline().rstrip().split(' ')]

cnt=0
for x in a:
    if is_prime(x) is True:
        cnt+=1

print(cnt)