a = input()
b = hex(a).upper
print('{:b},{:o},{},{:x},{},{}'.format(int(a), int(a), oct(int(a)), int(a),
                                       hex(int(a)), b))
