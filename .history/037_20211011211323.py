def main():
    n = int(input())
    M = n
    while M > 10:
        M = M // 10
    for A in range(1000, 10001):
        for B in range(1, 100):
            if ((A % B == 1) and (A // 100 - M * B < 10)
                    and (A // 100 - M * B > 0) and (A // B == n)
                    and ((A // 100 - M * B) * 100 + A % 100 > 100)):
                print(A, B)


main()
