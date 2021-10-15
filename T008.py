a = float(input())
b = str('%.6f' % a) + '/' + str('%.2f' % a) + '/' + str('%.8f' % a) + '/' + \
    str('%e' % a) + '/' + str(format(a, ','))
print(b)
