import cmath
x = int(input())
y = int(input())
cn = complex(x, y)
print(cmath.polar(cn)[1])
