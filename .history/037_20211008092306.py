q = int(input())
for f in range(1000, 10000):
    for d in range(10, 100):
        if d * q + 1 == f:
            print(f, d)
