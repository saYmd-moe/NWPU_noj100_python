dic2 = [2, 4, 8, 6]
dic3 = [3, 9, 7, 1]
dic4 = [4, 6, 4, 6]
dic7 = [7, 9, 3, 1]
dic8 = [8, 4, 2, 6]
dic9 = [9, 1, 9, 1]
a, b = map(int, input().split())
while (0 < a and 0 < b):
    if (a == 1 or a % 10 == 5 or a % 10 == 6):
        print(a % 10)
    if (a % 10 == 2):
        print(dic2[b % 4 - 1])
    if (a % 10 == 3):
        print(dic3[b % 4 - 1])
    if (a % 10 == 4):
        print(dic4[b % 4 - 1])
    if (a % 10 == 7):
        print(dic7[b % 4 - 1])
    if (a % 10 == 8):
        print(dic8[b % 4 - 1])
    if (a % 10 == 9):
        print(dic9[b % 4 - 1])
    a, b = map(int, input().split())
