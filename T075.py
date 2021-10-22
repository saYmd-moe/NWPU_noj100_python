L1 = input().split(' ')
L2 = input().split(' ')
dict = {}
dict = dict.fromkeys(L1)

for i in range(len(L2)):
    dict[L1[i]] = L2[i]

print(dict)
