n = input()
c = 0
while True:
    b = 0
    a = list(n)
    for i in range(len(n)):
        a[i] = int(a[i])
    for i in range(len(n)):
        b = a[i] + b
    n = int(n) - b
    c = c + 1
    if not n:
        print(c)
        break
    n = str(n)
    