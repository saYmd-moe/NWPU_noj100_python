from math import pow

v = float(input())
T = float(input())
print(
    round(13.12 + 0.6215 * T - 11.35 * pow(v, 0.16) +
          0.3965 * T * pow(v, 0.16)))
