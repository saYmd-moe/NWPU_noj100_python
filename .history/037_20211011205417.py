q = int(input())
qh = q // 100
qt = q // 10 % 10
qn = q % 100 % 10
for d in range(10, 100):
    f = d * q + 1
    ft = f