from sys import stdin

a = int(stdin.readline().rstrip())

for i in reversed(range(1, a+1)):
    print(i)