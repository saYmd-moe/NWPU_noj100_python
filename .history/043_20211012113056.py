def CollatzCalculate(n, a):
    a.append(n)    
    if n % 2 == 0:
        n = int(n / 2)
    if n % 2 == 1:
        n = 3 * n + 1


def main():
    n = int(input())
    a = []
    while n != 1:
        CollatzCalculate(n, a)
    print(''.join(str(i) for i in))