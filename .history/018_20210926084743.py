from math import sin, cos, acos

a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())
hav = sin((a2 - a1) / 2)**2 + cos(a1) * cos(a2) * (sin((b2 - b1) / 2)**2)
x = 1 - 2 * hav
d = acos(x) * 6371
print('{:.4f}km'.format(d))