def Del_a(a):
    for i in range(len(a)):
        a[i] = int(a[i].strip('a'))
    return a


def Add_a(a):
    for i in range(len(a)):
        a[i] = 'a' + str(a[i])
    return a


a = input().split(',')
a = Del_a(a)
a.sort()
a = Add_a(a)
print(' '.join(a))
