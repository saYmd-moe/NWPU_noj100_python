def main(M, N):
    if M <= 1 and n <= 0:
        return 0
    if M < N:
        return main(M, M)
    else:
        return main(M - N, N) + main(m, n - 1)
