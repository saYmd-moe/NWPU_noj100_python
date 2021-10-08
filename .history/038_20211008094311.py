n = int(input())
result = []
for a1 in range(n, ):
    for a2 in range(0, n + 1):
        if (a1 + a2) % 2 == 0:
            for a3 in range(0, n + 1):
                if (a2 + a3) % 3 == 0:
                    if (a1 + a2 + a3) % 5 == 0:
                        result.append(a1 + a2 + a3)
                    else:
                        continue
                else:
                    continue
        else:
            continue
print(max(result))
