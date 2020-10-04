l = [a+1 for a in range(10000)]

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                n = 1001*a + 101*b + 11*c + 2*d
                try:
                    l.pop(l.index(n))
                except:
                    pass

for x in l:
    print(x)
