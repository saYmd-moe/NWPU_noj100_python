def combination(n, m):
    result = 1
    for j in range(1, m + 1):
        result = result * (n - m + j) // j
    return result


