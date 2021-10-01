def C(n, m):
    # n <= m
    Min = min(n, m - n)
    result = 1
    for j in range(Min):
        result = result * (m - j) / (Min - j)
    return result


bi, bj, pi, pj = map(int(), input().split())