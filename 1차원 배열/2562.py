from sys import stdin


l = []
for i in range(9):
    tmp = stdin.readline().rstrip()
    l.append(int(tmp))

print(max(l))
print(l.index(max(l))+1)
