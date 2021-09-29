n = int(input())
b = 0
for i in range(1, n):
    if n // (5**i) == 0:
        for a in range(0, i):
            b = b + n // (5**a)
        break
print(b)
