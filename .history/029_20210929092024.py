n = input()
m = len(n)
n = list(n)
if m % 2 == 0:
    for i in range(0, m / 2):
        if n[i] == 6:
            if n[m - 1 - i] != 9:
                print('No')
                break
        if n[i] == 9:
            if n[m - 1 - i] != 6:
                print('No')
                break
        if n[i] == 0:
            if n[m - 1 - i] != 0:
                print('No')
                break
        if n[i] == 8:
            if n[m - 1 - i] != 8:
                print('No')
                break
        if n[i] == 1:
            if n[m - 1 - i] != 1:
                print('No')
                break


