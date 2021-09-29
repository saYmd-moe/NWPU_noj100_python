n = input()
m = int(input())
a = ''
while len(n) <= m:
    a = n + a
    n = int(n) + int(a)
    n = str(n)
print(n)
