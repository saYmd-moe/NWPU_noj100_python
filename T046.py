n = int(input())
n = '{:b}'.format(n)
length = len(n) - 1
n = list(n)
result = []
for i in range(length, -1, -1):
    result.append(n[i])
print(''.join(result))
