class Sentence():
    def __init__(self, L):
        self.s = L
        pass

    def reversed(self):
        self.s.reverse()
        print(' '.join(self.s))
        return None


a = Sentence(input().split(' '))
a.reversed()
