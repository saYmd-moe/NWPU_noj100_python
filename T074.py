a = input().split(' ')
b = input().split(' ')
c = a + b
c = list(set(c))
c.sort()
print(' '.join(c))
