n = input()
while True:
    b = 0
    a = list(n)
    for i in range(0, a):
        b = a[i] + b
    if not b:
        print(b)
        break
