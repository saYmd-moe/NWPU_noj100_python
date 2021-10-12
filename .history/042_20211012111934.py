def F(n):
    if n == 0:
        return 1
    else:
        return n - M(F(n - 1))
