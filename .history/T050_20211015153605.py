def main(M, N):
    if m <= 1 or n <= 0:
        return 0
    if M < N:
        return main(M, M)
    else:
        return main(M - N, N) + main(m, n - 1)