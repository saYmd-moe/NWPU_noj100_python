n = input()
b = 0
while True:
    a = list(n)
    for i in range(0, a):
        b = a[i] + b
    if not b:
        print(b)
        break
    n = str(n)
