from sys import stdin

n = stdin.readline().rstrip()
s = stdin.readline().rstrip().split(' ')

s = [float(x) for x in s]
m = max(s)

s = [x/m*100 for x in s]

print(sum(s)/len(s))
