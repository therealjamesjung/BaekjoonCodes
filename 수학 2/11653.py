n = int(input())

factor = 2
while True:
    if n == 1:
        break

    if n % factor == 0:
        print(factor)
        n = int(n / factor)
        factor = 2
    else:
        factor += 1
