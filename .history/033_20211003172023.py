from fractions import Fraction


n, a, b = map(int, input().split())
F1 = Fraction(a, b)
for down in range(n - 1, 0, -1):
    for up in range(n - 2, 0, -1):
        F2 = Fraction(up, down)
        if F2 < F1:
            print(F2)
            exit()
