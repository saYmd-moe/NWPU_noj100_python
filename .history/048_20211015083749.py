n = int(input())
if n == 0 or n == 1:
    print(1)
else:
    result = 0
    for k in range(2, n + 1):
        result += int((n + 2) / 2