def CollatzCalculate(n):
    if n % 2 == 0:
        n = int(n / 2)
    if n % 2 == 1:
        n = 3 * n + 1
    return n



n = int(input())
a = []
while n != 1:
    n = CollatzCalculate(n)
        a.append(n)
    print(','.join(str(i) for i in a))


main()
