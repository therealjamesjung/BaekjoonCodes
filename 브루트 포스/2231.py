from itertools import product

N = int(input())
n = N

k = 1

while True:
    if n < 1:
        break
    n = int(n / 10)
    k += 1

X = 0

for i in range(k - 1):
    X += (10 ** i) + 1

l = list()

for i in range(k - 1):
    lim = N // ((10 ** i) + 1)
    if lim > 9:
        lim = 9
    tmp = [a for a in range(lim + 1)]
    l.append(tmp)

answer = list()

for case in list(product(*l)):
    tmp = 0
    for i, a in enumerate(case):
        tmp += ((10 ** i) + 1) * a

    if tmp == N:
        answer.append(int(''.join(str(c) for c in list(case))[::-1]))

try:
    print(min(answer))
except ValueError:
    print(0)
