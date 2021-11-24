def f(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return f(k - 2) + f(k - 1)


n, k = map(int, input().split(' '))
count = 0
i = 1
while True:
    if f(i) % k == 0:
        count += 1
    i += 1
    if count == n:
        print(i - 1)
        break
