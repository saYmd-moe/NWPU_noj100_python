from math import sin, cos, acos, radians  # 经纬度转化为弧度

a1 = radians(float(input()))
b1 = radians(float(input()))
a2 = radians(float(input()))
b2 = radians(float(input()))
hav = sin((a2 - a1) / 2)**2 + cos(a1) * cos(a2) * (sin((b2 - b1) / 2)**2)
x = 1 - 2 * hav
d = acos(x) * 6371
print('{:.4f}km'.format(d))
