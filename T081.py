class Rectangle:
    def __init__(self, L, W):
        self.L = L
        self.W = W

    def area(self):
        return self.L * self.W


l, w = map(int, input().split(' '))
R = Rectangle(l, w)
print(R.area())
