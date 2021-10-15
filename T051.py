from re import search

while True:
    char = input()
    if len(char) < 3:
        if len(char) == 0:
            break
        else:
            print(char)
    else:
        if search('ing', char):
            print(char + 'ly')
        else:
            print(char + 'ing')
