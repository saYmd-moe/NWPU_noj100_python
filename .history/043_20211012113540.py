def CollatzCalculate(n, a, b):
    a.append(n)
    if n == 1:
        return False
    if n % 2 == 0:
        n = int(n / 2)
    if n % 2 == 1:
        n = 3 * n + 1
    return n


def main():
    n = int(input())
    a = []
    while n:
        n = CollatzCalculate(n, a, b)
    print(','.join(str(i) for i in a))


main()
