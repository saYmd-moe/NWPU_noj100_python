def pow(x, n):
    result = 1
    if n == 0:
        return 1
    elif n > 0:
        for i in range(n):
            result *= x
        return result
    else:
        for i in range(0, n, -1):
            result *= x
        result = 1 / result
        return result


x, n = map(int, input().split(' '))
print(pow(x, n))
