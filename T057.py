while True:
    phonenum = list(input())
    if phonenum == []:
        break
    if len(phonenum) != 11:
        print('False')
    else:
        try:
            i = 0
            while i < len(phonenum):
                phonenum[i] = int(phonenum[i])
                i += 1
            if phonenum[:2][0] == 1:
                if phonenum[:2][1] == 3 or phonenum[:2][1] == 4 \
                    or phonenum[:2][1] == 5 or phonenum[:2][1] == 7 or \
                        phonenum[:2][1] == 8 or phonenum[:2][1] == 9:
                    print('True')
                    continue
            print('False')
        except ValueError:
            print('False')
