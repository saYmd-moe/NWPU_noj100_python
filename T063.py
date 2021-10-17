m, n = map(int, input().split(' '))
a = input().split(' ')
a = a[m: n]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)
