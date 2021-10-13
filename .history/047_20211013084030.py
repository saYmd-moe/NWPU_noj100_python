def NextStep(x, y, n):
    if n == 1:
        x = x + y
    else:
        y = x + y


x1, y1, x2, y2 = map(int, input().split(' '))
x3, y3 = x1, y1
m = []
n = 1
while x1 < x2 and y1 < y2:  # 初始化列表m
    NextStep(x1, y1, n)
    m.append(1)
while m[0] == 1:
    x1, y1 = x3, y3
    for i in m:
        