n = input()
m = int(input())
a = n
while len(n) <= m:
    n = int(n) + int(n + a)
    n = str(n)
print(n)