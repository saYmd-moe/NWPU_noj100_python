list1 = list(input().split(' '))
list2 = list(input().split(' '))
result = []

for i in list1:
    if i not in list2:
        result.append(i)
for i in list2:
    if i not in list1:
        result.append(i)

result.sort()
print(' '.join(result))
