from fractions import Fraction


n, a, b = map(int, input().split())
for down in range(n, 0, -1):
    for up in range(n - 1, 0, -1):
        if up % down == 0:
            if Fraction(up, down) < Fraction(a, b):
                print(Fraction(up, down))
                break
