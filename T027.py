def main():
    n = int(input()) - 1
    a = [1, 1]
    if n <= 1:
        print('1')
    else:
        for i in range(1, n):
            b = a[i] + a[i - 1]
            a.append(b)
        print(b)


main()
