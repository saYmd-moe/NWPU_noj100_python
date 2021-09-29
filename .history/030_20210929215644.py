n = input()
b = 0
while True:
    a = len(n)
    n = int(n)
    n = n - a
    b = b + 1
    if not n:
        print(b)
        break
    n = str(n)
