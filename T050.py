def main(M, N):
    if M <= 1 or N <= 1:
        return 1
    if M < N:
        return main(M, M)
    else:
        return main(M - N, N) + main(M, N - 1)


M, N = map(int, input().split())
print(main(M, N))
