a = input().split(' ')
for i in range(len(a)):
    a[i] = int(a[i])
a.sort()
a.reverse()
for i in range(len(a)):
    a[i] = str(a[i])
print(' '.join(a))
