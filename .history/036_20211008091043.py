def main(n, m):
    result = 0
    if n == 0:
        result = m + 1
    else:
        result = 2 * main(n - 1, m)
    return result


while True:
    n, m = map(int, input().split(','))
    if n < 0 or m < 0:
        break
    else:
        main(n, m)