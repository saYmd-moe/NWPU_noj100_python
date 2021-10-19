def Cut(a):
    b = []

    for i in a:
        if i not in b:
            b.append(i)

    return b


def Count(a, b):
    c = []

    for i in b:
        c.append(0)

    for i in range(len(b)):

        for i1 in a:
            if b[i] == i1:
                c[i] += 1

    return c


def Output(b, c):

    for i in range(len(b)):
        if c[i] != 1:
            print('{} {}'.format(b[i], c[i]))
        else:
            continue

    pass


def main():
    a = input()
    b = Cut(a)
    c = Count(a, b)
    Output(b, c)


main()
