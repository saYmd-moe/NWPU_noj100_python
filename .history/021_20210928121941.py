n = input()
m = int(input())
a = ''
b = n
while len(n) < m:
    a = b + a
    n = int(n) + int(a)
    n = str(n)
print(n)
