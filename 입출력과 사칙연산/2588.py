A = input()
B = input()
for b in B[::-1]:
    print(eval(A+'*'+b))
print(eval(A+'*'+B))