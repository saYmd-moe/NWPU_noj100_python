q = int(input())
for d in range(10, 100):
    if 100 > (int(q / 100) * d) and (int(q / 100) * d) > 9 and int(
            q % 10) * d >= 100:
        f = d * q + 1
        print(f, d)
