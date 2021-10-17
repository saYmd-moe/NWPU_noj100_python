while True:
    char = list(input())
    if char == []:
        break
    else:
        i = 0
        a = len(char)
        while i < a:
            if i % 2 != 0:
                char[i] = ''
            i += 1
        print(''.join(char))
