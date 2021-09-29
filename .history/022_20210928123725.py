from math import sqrt

x = [0, 0, 0]
y = [0, 0, 0]
for i in range(3):
    x[i] = int(input())
    y[i] = int(input())
a = 2 * (x[1] - x[0])
b = 2 * (y[1] - y[0])
c = 2 * (x[2] - x[1])
d = 2 * (y[2] - y[1])
e = x[1] * x[1] + y[1] * y[1] - x[0] * x[0] - y[0] * y[0]
f = x[2] * x[2] + y[2] * y[2] - x[1] * x[1] - y[1] * y[1]
x1 = (b * f - d * e) / (b * c - d * a)
y1 = (c * e - a * f) / (b * c - d * a)
r = sqrt((x1 - x[0]) * (x1 - x[0]) + (y1 - y[0]) * (y1 - y[0]))
print('{:.3f},{:.3f},{:.3f}'.format(r, x1, y1))
