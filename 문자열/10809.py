from sys import stdin
import string

a = stdin.readline().rstrip()

l = [x for x in string.ascii_lowercase]

for x in l:
    try:
        print(a.index(x), end=" ")
    except:
        print('-1', end=" ")
