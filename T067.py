def Get_List():
    a = input().split(';')

    for i in range(len(a)):
        a[i] = eval(a[i])

    return a


def Sort_List(a):
    b = []

    for i in range(len(a)):
        b.append(a[i][len(a[i]) - 1])

    b.sort()
    c = []
    for i in b:
        c.append(i)

    for i1 in range(len(b)):
        for i2 in range(len(a)):
            if a[i2][len(a[i2]) - 1] == b[i1]:
                c[i1] = a[i2]
        else:
            continue

    return c


a = Get_List()
print(Sort_List(a))
