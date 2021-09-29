n = input()
m = len(n)
n = list(n)
for i in range(0, int(m / 2)):
    if n[i] == 6:
        if n[m - 1 - i] != 9:
            print('No')
            break
        else:
            continue
    if n[i] == 9:
        if n[m - 1 - i] != 6:
            print('No')
            break
        else:
            continue
    if n[i] == 0:
        if n[m - 1 - i] != 0:
            print('No')
            break
        else:
            continue
    if n[i] == 8:
        if n[m - 1 - i] != 8:
            print('No')
            break
        else:
            continue
    if n[i] == 1:
        if n[m - 1 - i] != 1:
            print('No')
            break
        else:
            continue
