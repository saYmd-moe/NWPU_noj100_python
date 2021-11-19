n = int(input())
lis = []
for i in range(n):
    line = input().split()
    lis.extend(line)
res = []
for i in range(n):
    if 0 == i:
        for j in range(n):
            res.append(lis[j])
    elif n - 1 == i:
        for j in range(n * (n - 1), n * n):
            res.append(lis[j])
    else:
        res.append(lis[(i + 1) * (n - 1)])
print(" ".join(res))
