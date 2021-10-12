def CollatzCalculate(n, a):
    a.append(n)
    
    if n % 2 == 0:
        n = n / 2
    if n % 2 == 1:
        n = 