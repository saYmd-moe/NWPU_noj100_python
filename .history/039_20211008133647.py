stick = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
n = int(input()) - 4
result = 0
for i1 in range(0, 10):
    for i2 in range(0, 10):
        i3 = i1 + i2
        if i1 + i2 < 10:
            if stick[i1] + stick[i2] + stick[i3] == n:
                result = result + 1
        if i1 + i2 >= 10:
            if stick[i1] + stick[i2] + stick[i3 % 10] + 2 == n:
                result = result + 1
print(result)
