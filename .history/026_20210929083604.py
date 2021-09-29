from fractions import Fraction

x = []
y = []
for i in range(0, 4):
    x.append(int(input()))
    y.append(int(input()))
x1 = Fraction(y[0] - y[1], x[0] - x[1])
x2 = Fraction(y[3] - y[2], x[3] - x[2])
if x1 == x2:
    print('Yes')
else:
    print('No')
