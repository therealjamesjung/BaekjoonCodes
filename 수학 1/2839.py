from sys import stdin

n = int(stdin.readline().rstrip())

flag = False
for i in range(n//5 + 1)[::-1]:
    if ((n-(i*5))%3) == 0:
        print(i + (n-i*5)//3)
        flag = True
        break

if flag is not True:
    print(-1)