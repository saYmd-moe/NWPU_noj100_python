class circle():
    def __init__(self, r):
        self.r = r
        self.a = 3.14 * self.r ** 2
        self.p = 2 * 3.14 * self.r

    def area(self):
        return '{:.2f}'.format(self.a)

    def perimeter(self):
        return '{:.2f}'.format(self.p)


c = circle(float(input()))
print(c.area(), c.perimeter())
