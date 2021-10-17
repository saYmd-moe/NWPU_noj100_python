def delete_(a):
    while True:
        try:
            a.remove('')
        except ValueError:
            return a


a1 = input().split(' ')
a2 = input().split(' ')
for i1 in range(0, len(a1)):
    for i2 in range(0, len(a2)):
        if a1[i1] == a2[i2]:
            a1[i1] = ''
            a2[i2] = ''
a1 = delete_(a1)
a2 = delete_(a2)
if a1 == [] and a2 == []:
    print(' '.join(a1), ' '.join(a2))
elif a1 == [] and a2:
    print(' '.join(a2))
elif a1 and a2 == []:
    print(' '.join(a1))
else:
    print('')
