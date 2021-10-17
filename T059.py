while True:
    char = list(input())
    if char == []:
        break
    if len(char) < 2:
        print(''.join(char))
        continue
    result = [char[0], char[1], char[len(char) - 2], char[len(char) - 1]]
    print(''.join(result))
