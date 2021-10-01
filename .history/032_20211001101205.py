def C(n, m):
    # n <= m
    Min = min(n, m - n)
    result = 1
    for j in range(Min):
        result = result * (m - j) / (Min - j)
    return int(result)


bi, bj, pi, pj = map(int(), input().split())
if bi < 0 or pi < 0 or bj < 0 or pj < 0 or bi < pi or bj < pj:
    exit()
else:
    result = C(bi, bi + bj) - (C(pi, pi + pj) * C(bi - pi, bi + bj - pi - pj))
