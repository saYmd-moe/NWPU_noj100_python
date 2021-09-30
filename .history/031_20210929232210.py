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


a1, a2 = input().split()
b1, b2 = input().split()
c1, c2 = input().split()
d1, d2 = input().split()
a2 = 
b2 = 
c2 = 
d2 = 
if a1 <= 0:
    print(end='')
else:
    main(int(list(a1)[len(a1) - 1]), int(a2))
if b1 <= 0:
    print(end='')
else:
    main(int(list(b1)[len(b1) - 1]), int(b2))
if c1 <= 0:
    print(end='')
else:
    main(int(list(c1)[len(c1) - 1]), int(c2))
if d1 <= 0:
    print(end='')
else:
    main(int(list(d1)[len(d1) - 1]), int(d2))
