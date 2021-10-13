def NextStep(x, y, n):
    if n == 1:
        x = x + y
    else:
        y = x + y


x1, y1, x2, y2 = map(int, input().split(' '))
m = []
n = 1
while x1 < x2 and y1 < y2:  # 初始化列表m
    NextStep(x1, y1, n)
    m.append(1)
for i in 