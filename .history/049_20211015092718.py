n, v = map(int, input().split())

for i1 in range(0, v + 1):
    for i2 in range(0, v + 1):
        for i3 in range(0, v + 1):
            for i4 in range(0, v + 1):
                for i5 in range(0, v + 1):
                    if i1 + i2 + i3 + i4 + i5 ==