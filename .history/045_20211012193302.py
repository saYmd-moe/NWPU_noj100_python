def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


a, b = map(int, input().split())
x = 1
y = -1
while True:
    while True:
        if a * x + b * y == gcd(a, b):
            print(x, y)
            exit()
        b -= 1
    