def TurnAround(a):
    turned = []

    for i in range(len(a)):
        turned.append(a[len(a) - i - 1])

    return turned


def Add(a, b):
    c = []

    for i in range(len(a)):
        c.append(a[i] + b[i])

    return tuple(c)


a = input().split(' ')

for i in range(len(a)):
    a[i] = int(a[i])

turned = TurnAround(a)
print(Add(a, turned))
