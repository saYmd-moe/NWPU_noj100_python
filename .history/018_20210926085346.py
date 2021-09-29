from math import sin, cos, acos, radians

a1 = radians((input()))
b1 = radians(input())
a2 = radians(input())
b2 = radians(input())
hav = sin((a2 - a1) / 2)**2 + cos(a1) * cos(a2) * (sin((b2 - b1) / 2)**2)
x = 1 - 2 * hav
d = acos(x) * 6371
print('{:.4f}km'.format(d))
