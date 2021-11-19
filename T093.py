L1 = input().split(' ')
L2 = input().split(' ')

for i in range(len(L2)):
    L2[i] = int(L2[i])

S = set(L2)
Ls0 = []
Ls1 = []
Ls2 = []

for i0 in S:
    Ls0.append([])
    for i1 in range(len(L2)):
        if i0 == L2[i1]:
            Ls0[len(Ls0) - 1].append(i1)

for Li0 in Ls0:
    Ls1.append([])
    for i in Li0:
        Ls1[len(Ls1) - 1].append(L1[i])
    Ls1[len(Ls1) - 1].sort()

for Li1 in Ls1:
    Ls2 += Li1

print(' '.join(Ls2))
