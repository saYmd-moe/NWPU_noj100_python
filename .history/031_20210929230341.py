def 给我康康你的个位数是什么(n):
    return int(list(n)[len(n) - 1])


def 让我康康你次方过的个位是什么(n, m):
    d2 = {1: 2, 2: 4, 3: 6, 0: 8}
    d3 = {1: 3, 2: 8, 3: 7, 0: 1}
    d4 = {1: 4, 0: 6}
    d5 = {1: 5, 0: 0}
    d7 = {1: 7, 2: 9, 3: 3, 0: 1}
    d8 = {1: 8, 2: 4, 3: 2, 0: 6}
    d9 = {1: 9, 0: 1}
    if n == 0:
        return ''
    elif m == 0:
        return ''
    elif n == 1:
        return 1
    elif n == 6:
        return 6
    elif n == 2:
        return d2[m % 4]
    elif n == 3:
        return d3[m % 4]
    elif n == 4:
        return d4[m % 2]
    elif n == 5:
        return d5[m % 2]
    elif n == 7:
        return d7[m % 4]
    elif n == 8:
        return d8[m % 4]
    elif n == 9:
        return d9[m % 2]


a1,a2 = input().split()
b1, b2 = input().split()
c1, c2 = input().split()
d1, d2 = input().split()
