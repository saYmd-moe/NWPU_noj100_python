def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


a, b = map(int, input().split())
for x in range(0, 100):
    for y in range(0):
        if a * x + b * y == gcd(a, b):
            print(x, y)
            exit()
