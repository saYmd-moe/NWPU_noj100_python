n = int(input())
a = []

for i in range(1, n + 1):
    a.append('{}: {}'.format(i, i * i))

a = eval('{' + ', '.join(a) + '}')
print(a)
