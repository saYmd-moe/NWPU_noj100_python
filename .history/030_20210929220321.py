n = input()
c = 0
for i in range(0, len(n)):
    n[i] = int(n[i])
while True:
    b = 0
    a = list(n)
    for i in range(0, len(n)):
        b = a[i] + b
    n = b
    c = c + 1
    if not n:
        print(c)
        break
