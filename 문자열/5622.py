from sys import stdin

a = stdin.readline().rstrip()

n = {
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z'],
}

s = 0

for x in a:
    for k, v in n.items():
        try:
            v.index(x)
            s += k+1
        except:
            pass

print(s)
