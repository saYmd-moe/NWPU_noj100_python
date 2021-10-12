q = int(input())
qh = q // 100
qt = q % 100 // 10
qn = q % 100 % 10
for d in range(10, 100):
    if d * qn >= 100 and d * qn < 1000 and d * qh < 100:
        print(d * q +1)
