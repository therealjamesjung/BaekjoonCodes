A = input().split(' ')
h = int(A[0])
m = int(A[1])

if m>=45:
    print(str(h)+' '+str(m-45))
else:
    if h==0:
        h=24
    print(str(h-1)+' '+str(m+15))