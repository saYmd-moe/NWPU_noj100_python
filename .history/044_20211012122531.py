def dfs(a, b):
    if a == 1:
        return 1
    if b == 1:
        return 0
    if a % m == 0:
        return dfs(a, b - 1) + dfs(a / b, b)
    return dfs(a, b - 1)