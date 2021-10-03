while True:
    n = int(input())
    i = 0
    if n == 0:
        break
    else:
        for D1 in range(1, 3):
            if D1 == n:
                i = i + 1
            for D2 in range(1, 3):
                if D1 + D2 == n:
                    i = i + 1
                for D3 in range(1, 3):
                    if D1 + D2 + D3 == n:
                        i = i + 1
                    for D4 in range(1, 3):
                        for D5 in range(1, 3):
                            for D6 in range(1, 3):
                                for D7 in range(1, 3):
                                    for D8 in range(1, 3):
                                            for D9 in range(1, 3):
                                                for D10 in range(1, 3):
                                                    for D11 in range(1, 3):
                                                        for D12 in range(1, 3):
                                                            for