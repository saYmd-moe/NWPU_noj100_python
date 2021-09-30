def 给我康康你的个位数是什么(n):
    return int(list(n)[len(n) - 1])


def 让我康康你次方过的个位是什么(n, m):
    d2 = {1: 2, 2: 4, 3: 6, 4: 8}
    if n == 0:
        return ''
    elif m == 0:
        return ''
    elif n == 1:
        return 1
    elif n == 2:

