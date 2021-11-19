c1, c2 = map(str, input().split(' '))
c1, c2 = set(c1), set(c2)
c = 0
for i0 in c1:
    for i1 in c2:
        if i0 == i1:
            c += 1
            continue
print(c)
