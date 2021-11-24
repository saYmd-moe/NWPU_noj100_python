T12 = input().split(' ')
T24 = T12[0].split(':')
if int(T24[0]) == 12 and T12[1] == 'AM':
    T24[0] = '00'
elif int(T24[0]) != 12 and T12[1] == 'PM':
    T24[0] = str((int(T24[0]) + 12) % 24)
print(':'.join(T24))
