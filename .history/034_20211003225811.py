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
                        if D1 + D2 + D3 + D4 == n:
                            i = i + 1
                        for D5 in range(1, 3):
                            if D1 + D2 + D3 + D4 + D5 == n:
                                i = i + 1
                            for D6 in range(1, 3):
                                if D1 + D2 + D3 + D4 + D5 + D6 == n:
                                    i = i + 1
                                for D7 in range(1, 3):
                                    if D1 + D2 + D3 + D4 + D5 + D6 + D7 == n:
                                        i = i + 1
                                    for D8 in range(1, 3):
                                        if D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8 == n:
                                            i = i + 1
                                        for D9 in range(1, 3):
                                            if D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8 + D9 == n:
                                                i = i + 1
                                            for D10 in range(1, 3):
                                                if D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8 + D9 + D10 == n:
                                                    i = i + 1
                                                for D11 in range(1, 3):
                                                    if D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8 + D9 + D10 + D11 == n:
                                                        i = i + 1
                                                    for D12 in range(1, 3):
                                                        if D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8 + D9 + D10 + D11 + D12 == n:
                                                            i = i + 1
                                                        for D13 in range(1, 3):
                                                            if D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8 + D9 + D10 + D11 + D12 + D13 == n:
                                                                i = i + 1
                                                            for D14 in range(
                                                                    1, 3):
                                                                if D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8 + D9 + D10 + D11 + D12 + D13 + D14 == n:
                                                                    i = i + 1
                                                                for D15 in range(
                                                                        1, 3):
                                                                    if D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8 + D9 + D10 + D11 + D12 + D13 + D14 + D15 == n:
                                                                        i = i + 1
                                                                    for D16 in range(
                                                                            1,
                                                                            3):
                                                                        if D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8 + D9 + D10 + D11 + D12 + D13 + D14 + D15 + D16 == n:
                                                                            i = i + 1
                                                                        for D17 in range(
                                                                                1,
                                                                                3
                                                                        ):
                                                                            if D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8 + D9 + D10 + D11 + D12 + D13 + D14 + D15 + D16 + D17 == n:
                                                                                i = i + 1
                                                                            for D18 in range(
                                                                                    1,
                                                                                    3
                                                                            ):
                                                                                if D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8 + D9 + D10 + D11 + D12 + D13 + D14 + D15 + D16 + D17 + D18 == n:
                                                                                    i = i + 1
                                                                                for D19 in range(
                                                                                        1,
                                                                                        3
                                                                                ):
                                                                                    if D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8 + D9 + D10 + D11 + D12 + D13 + D14 + D15 + D16 + D17 + D18 + D19 == n:
                                                                                        i = i + 1
                                                                                    for D20 in range(1, 3):
                                                                                        if D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8 + D9 + D10 + D11 + D12 + D13 + D14 + D15 + D16 + D17 + D18 + D19 == n:
                                                                                        i = i + 1
    print(i)
