from sys import stdin

n = int(stdin.readline().rstrip())

for i in range(n):
    a = stdin.readline().rstrip().split('X')
    score=0
    for data in a:
        if len(data) != 0:
            score += int((len(data))*(len(data)+1)/2)
    print(score)
