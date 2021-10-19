a = input().split(' ')

for i in range(len(a)):
    a[i] = int(a[i])

b = 1
for i in a:
    b *= i

print(b)
