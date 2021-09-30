def main(a, b):
    if a == 0:
        return ''
    elif b == 0:
        return ''
    c = int(list(a)[len(a) - 1]) ** b
    return list(c)[len(c) - 1]


a1, a2 = input().split()
b1, b2 = input().split()
c1, c2 = input().split()
d1, d2 = input().split()
print(main(a1, a2))
print(main(b1, b2))
print(main(c1, c2))
print(main(d1, d2))
