from itertools import combinations


class NUM():
    def __init__(self, L):
        self.L = list(combinations(L, 3))
        for i in range(len(self.L)):
            self.L[i] = list(self.L[i])

    def IsItZero(self):
        result = []
        for i in self.L:
            if sum(i) == 0:
                result.append(i)
        return result


a = input().split(' ')
for i in range(len(a)):
    a[i] = int(a[i])
a = NUM(a)
print(a.IsItZero())
