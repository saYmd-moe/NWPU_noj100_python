from os import system

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
D = a * e - d * b
if D == 0:
    print('error')
    system.exit()
D1 = c * e - b * f
D2 = a * f - d * c

