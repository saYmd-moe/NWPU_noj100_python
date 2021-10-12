pells = [0, 1]
n = int(input()) - 1
a = 2
while a <= n:
    b = 2 * pells[a - 1] + pells[a - 2]
    pells.append(b)
    a += 1
print(pells[n + 1])
