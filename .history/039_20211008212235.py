def stick(num):
    stick_num = {0: 6, 1: 2, 2: 5, 3: 5, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    num_list = list(str(num))
    for i in num_list:
        result = result + stick_num.get(i)
    return result


n = int(input()) - 4
for i1 in range(0, 1000):
    for i2 in range(0, 1000):
        if 
