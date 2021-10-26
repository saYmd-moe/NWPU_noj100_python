keys = []
values = []

while True:
    st = input().split(' ')
    if st == ['']:
        break
    else:
        keys.append(st[0])
        values.append(st[1])

dic = dict(zip(keys, values))
print(list(sorted(dic.items(), key=lambda dic: dic[1], reverse=False)))
print(list(sorted(dic.items(), key=lambda dic: dic[0], reverse=True)))
