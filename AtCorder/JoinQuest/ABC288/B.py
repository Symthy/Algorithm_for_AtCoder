N, K = map(int, input().split())
S = []
for _ in range(N):
    S.append(input())

s_sorted = sorted(S[:K])
for i in range(K):
    print(s_sorted[i])
