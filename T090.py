def ANtoRN(n):
    Units = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    Tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    Hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    Thousands = ['', 'M', 'MM', 'MMM']
    n = n.zfill(4)
    rs = Thousands[int(n[0])] + Hundreds[int(n[1])] + Tens[int(
        n[2])] + Units[int(n[3])]
    return rs


print(ANtoRN(input()))
