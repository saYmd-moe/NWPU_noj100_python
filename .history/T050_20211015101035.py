def main(M, N):
    if M < N:
        return main(M, M)
    else:
