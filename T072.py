a = input().split(',')
b = []

for i in a:
    b.append(i.split(':'))

c = []

for i in b:
    c.append(int(i[1]))

print(max(c), min(c))
