n = int(input())
i = 0
for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                if a + b + c + d == n:
                    i = i + 1
print(i)
