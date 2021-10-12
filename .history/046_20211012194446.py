n = int(input())
n = '{:b}'.format(n)
length = len(n) - 1
n = list(n)
for i0 in range(length, 0, -1):
    i1 = length - i0
    n[i0], n[i1] = n[i1], n[i0]
print(''.join(n))
