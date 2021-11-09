a = input().split(' ')
b = []
for i in range(len(a)):
    b.append('')
n = int(input())
for i in range(len(a)):
    b[i - n] = a[i]
print(' '.join(b))
