def solve1():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    L = []
    R = []

    Q = int(input())
    for i in range(Q):
        l, r = map(int, input().split())
    L.append(l)
    R.append(r)

    dp = [[0] * (K) for _ in range(N + 1)]
    for i in range(1, N + 1):
        dp[i][(i - 1) % K] += A[i - 1]
    for i in range(1, N + 1):
        for j in range(K):
            dp[i][j] += dp[i - 1][j]

    for i in range(Q):
        array = [dp[R[i]][j] - dp[L[i] - 1][j] for j in range(K)]
    if len((set(array))) == 1:
        print("Yes")
    else:
        print("No")


from sys import stdin


def solve2():

    input = lambda: stdin.readline()[:-1]

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    cum = []
    for i in range(k):
        res = [0]
        for j in range(i, n, k):
            res.append(res[-1] + a[j])
        cum.append(res)

    q = int(input())
    for _ in range(q):
        l, r = map(lambda x: int(x) - 1, input().split())
    S = set()
    for i in range(k):
        L = (l - i + k - 1) // k
        R = (r - i) // k
        S.add(cum[i][R + 1] - cum[i][L])

    if len(S) == 1:
        print("Yes")
    else:
        print("No")
