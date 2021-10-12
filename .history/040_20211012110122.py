def stairs(n):
    a = [i for i in range(n + 3)]
    a[1] = 1
    a[2] = 2
    a[3] = 4
    for i in range(4, n + 1):
        a[i] = ((a[i - 1] + a[i - 2]) % 1000000007 + a[i - 3]) % 1000000007
        