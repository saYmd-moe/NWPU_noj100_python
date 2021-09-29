import cmath
x = int(input())
y = int(input())
cn = complex(x, y)
print('{:.4f},{:.4f}', format(cmath.polar(cn)[1]))
