n = input()
c = 0
while True:
    b = 0
    a = list(n)
    for i in range(0, a):
        b = a[i] + b
    n = b
    c = c + 1
    if not n:
        print(c)
        break
