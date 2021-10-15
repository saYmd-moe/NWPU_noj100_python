def dfs(a, b):
    if a == 1:
        return 1
    if b == 1:
        return 0
    if a % b == 0:
        return dfs(a, b - 1) + dfs(a / b, b)
    return dfs(a, b - 1)


a = int(input())
print(dfs(a, a))
