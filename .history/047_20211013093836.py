def OneStep(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 'true'
    if x1 > x2 or y1 > y2:
        return 'false'
    else:
        return OneStep(x1 + y1, y1, x2, y2) or OneStep(x1, x1 + y1, )