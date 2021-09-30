def main(n, m):
    d2 = {1: 2, 2: 4, 3: 6, 0: 8}
    d3 = {1: 3, 2: 8, 3: 7, 0: 1}
    d4 = {1: 4, 0: 6}
    d5 = {1: 5, 0: 0}
    d7 = {1: 7, 2: 9, 3: 3, 0: 1}
    d8 = {1: 8, 2: 4, 3: 2, 0: 6}
    d9 = {1: 9, 0: 1}
    if n == 0:
        print(0)
    elif m == 0:
        print(end='')
    elif n == 1:
        print(1)
    elif n == 6:
        print(6)
    elif n == 2:
        print(d2[m % 4])
    elif n == 3:
        print(d3[m % 4])
    elif n == 4:
        print(d4[m % 2])
    elif n == 5:
        print(d5[m % 2])
    elif n == 7:
        print(d7[m % 4])
    elif n == 8:
        print(d8[m % 4])
    elif n == 9:
        print(d9[m % 2])


a = 1
while a:
    n, m = input().split()
    if int(n) == 0:
        a = 0
        break
    elif int(m) == 0:
        a = 0
        break
    else:
        main(int(list(n)[len(n) - 1]), int(m))
