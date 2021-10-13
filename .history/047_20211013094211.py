def OneStep(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return True
    if x1 > x2 or y1 > y2:
        return False
    else:
        return OneStep(x1 + y1, y1, x2, y2) or OneStep(x1, x1 + y1, x2, y2)


x1, x2, y1, y2 = map(int, input().split())
if OneStep(x1, x2, y1, y2):
    print('true')
else:
    print('false')
