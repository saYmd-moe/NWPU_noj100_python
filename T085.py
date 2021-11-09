from itertools import combinations


class SUCC():
    def __init__(self, L, n):
        self.L = list(combinations(L, 2))
        self.n = n

    def SUM(self):
        for i in self.L:
            if sum(i) == self.n:
                print('{} + {} = {}'.format(i[0], i[1], sum(i)))
                break


L = input().split(' ')
n = int(input())
for i in range(len(L)):
    L[i] = int(L[i])
a = SUCC(L, n)
a.SUM()
