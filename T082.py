from math import pow


class A:
    def __init__(self, _s):
        self.s = _s

    def fun(self):
        Len = len(self.s)
        ll = []
        for ii in range(0, int(pow(Len, 2) - 1)):
            lll = []
            for j in range(Len):
                if (ii >> j) % 2:
                    lll.append(self.s[Len - j - 1])
            lll.sort()
            ll.append(lll)
        if ll[-1] != self.s:
            ll.append(self.s)
        return ll


x = input()
l1 = x.split()
for i in range(0, len(l1)):  # 变为int
    l1[i] = int(l1[i])

s1 = set(l1)
l1 = list(s1)  # 去重
l1.sort(reverse=False)  # 排序
a = A(l1)
print(a.fun())
