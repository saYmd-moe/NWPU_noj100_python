from fractions import Fraction


n = int(input())
if n == 0 or n == 1:
    print(1)
else:
    result = Fraction(0)
    for k in range(2, n + 1):
        result += F(n + k) / k
    print(result)
