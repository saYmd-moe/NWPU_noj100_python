def Compare(a, b):

    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        else:
            return False

    return True


def GoingOn(a):
    b = []

    for i in a:
        b.append('')

    for i in range(len(a) - 1):
        b[i + 1] = a[i]

    b[0] = a[len(a) - 1]
    return b


def Exhaust(a, b):
    c = []

    for i in range(len(a)):
        a = GoingOn(a)
        c.append(Compare(a, b))

    for i in c:
        if not i:
            continue
        else:
            print('True')
            return None

    print('False')
    return None


a = input().split(' ')
b = input().split(' ')
Exhaust(a, b)
