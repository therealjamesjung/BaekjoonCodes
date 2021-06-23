n = int(input())

k = 0

"""
while True:
    if n == 1:
        break
    else:
        n = int(n / 3)
        k += 1 
"""

pattern = ['***', '* *', '@@@']

a = list()

for i in range(n):
    a.append(['*'] * n)


def square(n):
    if n <= 0:
        return

    # full
    print('*', end='')
    square(n - 1)
    print('@', end='')
    square(n - 1)
    print('#')
    # full

# square(n)
