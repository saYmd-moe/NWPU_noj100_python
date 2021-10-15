'''
from fractions import Fraction


n = int(input())
if n == 0 or n == 1:
    print(1)
else:
    result = Fraction(1)
    for k in range(2, n + 1):
        result *= Fraction(n + k, k)
    print(result)
'''
n = int(input())
if n == 0 or n == 1:
    print(1)
else:
    result = 1
    for k in range(2, n + 1):
        result *= (n + k) / k