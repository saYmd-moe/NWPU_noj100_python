def CollatzCalculate(n):
    if n % 2 == 0:
        re int(n / 2)
    if n % 2 == 1:
        n = 3 * n + 1
    return n


n = int(input())
a = []
while n != 1:
    a.append(n)
    n = CollatzCalculate(n)
print(','.join(str(i) for i in a))
