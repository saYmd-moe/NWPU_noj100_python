x = []
y = []
for i in range(1, 7):
    x[i - 1] = int(input())
    y[i - 1] = int(input())
a = 2 * (x[1] - x[0])
b = 2 * (y[1] - y[0])
c = 2 * (x[2] - x[1])
d = 2 * (y[2] - y[1])
e = x[1] *x[1] + y[1] * y[1] - x[0] * x[0] - y[0] * y[0]
