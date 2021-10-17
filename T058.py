char = list(input())
i = 0
while i < len(char):
    if char[i] == ',':
        char[i] = '.'
    elif char[i] == '.':
        char[i] = ','
    i += 1
print(''.join(char))
