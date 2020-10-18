from sys import stdin

def f(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    
    return f(x-2)+f(x-1)

n = int(stdin.readline())
print(f(n))