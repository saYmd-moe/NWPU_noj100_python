from fractions import Fraction


n, a, b = map(int, input().split())
c = []
F1 = Fraction(a, b)
for down in range(n - 1, 0, -1):
    for up in range(n - 2, 0, -1):
        F2 = Fraction(up, down)
        if F2 < F1:
            c.append(F2)
print(maximum(C))
