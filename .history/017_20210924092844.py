R = float(input())
G = float(input())
B = float(input())
mx = max(R, G, B)
mn = min(R, G, B)
V = mx
S = (mx - mn) / mx
if V == 0:
    S = 0
if mx == R:
    a = 0 + (G - B) / (mx - mn)
if mx == G:
    a = 2 + (B - G) / (mx - mn)
if mx == B:
    a = 4 + (R - G) / (mx - mn)
H = 60 * a
if H < 0:
    H = H + 360
print('{:.4f},{:.4f}%,{:.4f}%'.format(H, S * 100, V))
