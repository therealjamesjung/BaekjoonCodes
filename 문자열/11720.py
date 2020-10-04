from sys import stdin

a = stdin.readline().rstrip()
n = stdin.readline().rstrip()

a = [int(x) for x in n]
print(sum(a))
