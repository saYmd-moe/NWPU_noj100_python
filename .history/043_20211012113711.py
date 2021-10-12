def CollatzCalculate(n):
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
        a.append(CollatzCalculate(n))
    print(','.join(str(i) for i in a))


main()
