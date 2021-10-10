q = int(input())  # 商
d = int()  # 除数

for d in range(10, 100):
    if 100 > (int(q / 100) *
              d) > 9 and int(q % 10) * d >= 100:  #q的百位*d是两位数，q的个位*d是三位数
        f = d * q + 1  # 被除数
        print(f, ' ', d)