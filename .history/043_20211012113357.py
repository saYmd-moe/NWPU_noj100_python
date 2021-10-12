def CollatzCalculate(n, a, b):
    a.append(n)
    if n == 1:
        b = False
    if n % 2 == 0:
        n = int(n / 2)
    if n % 2 == 1:
        n = 3 * n + 1


def main():
    n = int(input())
    a = []
    b = True
    while b:
        CollatzCalculate(n, a, b)
    print(','.join(str(i) for i in a))


main()
