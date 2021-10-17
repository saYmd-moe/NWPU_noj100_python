n = input()
a = input().split(' ')
i, b = 0, 0
while i < len(a):
    if a[i] == n:
        b += 1
    i += 1
print(b)
