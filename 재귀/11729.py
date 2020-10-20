from sys import stdin

n = int(stdin.readline())

def hanoi(n, start, via, end):
    if n ==1:
        print(start, end)
    else:
        hanoi(n-1, start, end, via)
        print(start, end)
        hanoi(n-1, via, start, end)

print((2**n) - 1)
hanoi(n, 1, 2, 3)