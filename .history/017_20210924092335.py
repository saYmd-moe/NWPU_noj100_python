R = float(input())
G = float(input())
B = float(input())
mx = max(R, G, B)
mn = min(R, G, B)
V = mx
S = (mx - mn) / mx
if V == 0:
    S = 0
