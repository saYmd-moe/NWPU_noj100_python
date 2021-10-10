def stick(num):
    result = 0
    stick_num = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    num_list = list(str(num))
    for i in num_list:
        result = result + stick_num.get()
    return result


n = int(input()) - 4
count = 0
for i1 in range(0, 1000):
    for i2 in range(0, 1000):
        i3 = i1 + i2
        if i3 != 0:
            if stick(i1) + stick(i2) + stick(i3) == n:
                count += 1
print(count)
