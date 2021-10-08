q = int(input())
for d in range(10, 100):
    f = d * q + 1
    if f < 10000 and f >= 1000:
        print(F, d)
