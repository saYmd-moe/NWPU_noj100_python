def NextStep(x, y, n):
    global x1, y1
    if n == 1:
        x1 = x + y
    else:
        y1 = x + y


x1, y1, x2, y2 = map(int, input().split(' '))
x3, y3 = x1, y1
m0 = []
m1 = []
n0 = 1
n1 = 0
while x1 <= x2 and y1 <= y2:  # 初始化列表m
    NextStep(x1, y1, n0)
    m0.append(1)
x1, y1 = x3, y3
while x1 <= x2 and y1 <= y2:
    NextStep(x1, y1, n1)
    m1.append(0)
m0.append(0)
m1.append(1)
while m0[0] == 1:
    x1, y1 = x3, y3
    for i in m0:
        if x1 < x2 and y1 < y2:
            NextStep(x1, y1, i)
            if x1 == x2 and y1 == y2:
                print('True')
                exit()
    for i in range(len(m0)):
        if m0[i] == 0:
            m0[i - 1] = 0
while m1[0] == 0:
    x1, y1 = x3, y3
    m1.pop（
    for i in m1:
        if x1 < x2 and y1 < y2:
            NextStep(x1, y1, i)
            if x1 == x2 and y1 == y2:
                print('True')
                exit()
    for i in range(len(m1)):
        if m1[i] == 1:
            m1[i - 1] = 1
print('False')
