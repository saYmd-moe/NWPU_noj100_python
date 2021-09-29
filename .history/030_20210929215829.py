n = input()
b = 0
while True:
    a = list(n)
    for i in range(0, a):
        b = a[i] + b
    n = n - a
    b = b + 1
    if not n:
        print(b)
        break
    n = str(n)
