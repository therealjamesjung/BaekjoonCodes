A = input().split(' ')
a = int(A[0])
b = int(A[1])

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")