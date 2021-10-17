while True:
    ipv4 = input().split('.')
    if ipv4 == ['']:
        break
    if len(ipv4) != 4:
        print('False')
    else:
        try:
            for i in range(len(ipv4)):
                ipv4[i] = int(ipv4[i])
            if ipv4[0] <= 255 and ipv4[0] >= 0:
                if ipv4[1] <= 255 and ipv4[1] >= 0:
                    if ipv4[2] <= 255 and ipv4[2] >= 0:
                        if ipv4[3] <= 255 and ipv4[3] >= 0:
                            print('True')
                            continue
            raise SyntaxError
        except SyntaxError or ValueError:
            print('False')
