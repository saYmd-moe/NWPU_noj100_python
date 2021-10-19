s1 = input().split(' ')
s2 = input().split(' ')
result = []

for i in s1:
    if i in s2:
        result.append(i)
    else:
        continue

result.sort()
print(' '.join(result))

