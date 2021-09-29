from fractions import Fraction

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
f1 = Fraction(num1, num2)
f2 = Fraction(num3, num4)
F = '({}/{}){}({}/{})={}'
print(F.format(num1, num2, '+', num3, num4, f1 + f2))
print(F.format(num1, num2, '-', num3, num4, f1 - f2))
print(F.format(num1, num2, '*', num3, num4, f1 * f2))
print(F.format(num1, num2, '/', num3, num4, f1 / f2))