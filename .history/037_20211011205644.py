q = int(input())
qh = q // 100
qt = q // 10 % 10
qn = q % 100 % 10
for d in range(10, 100):
    f = d * q + 1
    if d * qh > 10 and d * qh < 100:
        ft = f // 10