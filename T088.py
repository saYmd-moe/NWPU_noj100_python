class utils:
    def __init__(self, st):
        self.st = st

    def changest(self, st):
        self.st = st

    def islegal(self):
        lis = []
        dic = {')': '(', ']': '[', '}': '{'}
        for i in range(len(self.st)):
            if self.st[i] == '(' or self.st[i] == '[' or self.st[i] == '{':
                lis.append(self.st[i])
            if self.st[i] == ')' or self.st[i] == ']' or self.st[i] == '}':
                if lis[len(lis) - 1] == dic[self.st[i]]:
                    lis.pop()
        if len(lis) == 0:
            print('True')
        else:
            print('False')


u = utils('')
while True:
    st = input()
    if st == '':
        break
    u.changest(st)
    u.islegal()
