x = input().split(' ')

if len(x[0]) > len(x[1]):
    a = x[0]
    b = x[1]
else:
    a = x[1]
    b = x[0]

index = 1
flag = 0

while True:
    try:
        add = int(b[index * -1]) + int(a[index * -1]) + flag
    except IndexError:
        if flag == 0:
            break
        try:
            add = int(a[index * -1]) + flag
        except IndexError:
            a = '1' + a
            break

    if add >= 10:
        a = a[:len(a) - index] + str(add % 10) + a[len(a) - index + 1:]
        flag = 1

    else:
        a = a[:len(a) - index] + str(add) + a[len(a) - index + 1:]
        flag = 0

    index += 1

print(a)
