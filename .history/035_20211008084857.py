s = [i for i in range(1001)]
s[0] = 1
s[2] = 3
for i in range(4, 1001, 2):
    s[i] = 4 * s[i - 2] - s[i - 4]
n = int(input())
while n > 0:
    if n == 0:
        print(0)
    else:
        print(s[n] % 100003)
    n = int(input())