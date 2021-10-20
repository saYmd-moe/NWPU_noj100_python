a = input().split(',')
b = []

for i in a:
    b.append(i.split(':'))

c = []

for i in b:
    c.append(i[1])

c.sort()
print(max(c), min(c))
