a = input()
b = str(hex(int(a))).upper
print('{:b},{:o},{},{:x},{},{}'.format(int(a), int(a), oct(int(a)), int(a), hex(int(a)), b))
