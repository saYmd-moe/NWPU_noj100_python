n = int(input())
for a1 in range(n, -1, -1):
    for a2 in range(n, -1, -1):
        if (a1 + a2) % 2 == 0:
            for a3 in range(n, -1, -1):
                if (a2 + a3)