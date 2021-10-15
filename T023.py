n = list(input())
m = []
for i in n:
    m.append(i)
m.reverse()
if m == n:
    print('Yes')
else:
    print('Not')
