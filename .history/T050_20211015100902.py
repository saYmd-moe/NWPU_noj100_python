def main(M, N):
    if M < N:
        return main(M, N - 1)
    else:
        