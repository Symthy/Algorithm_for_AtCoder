"""
in:
4 5 # 個数 容量
4 2 # 価値 重み
5 2
2 1
8 3

out:
13
"""


N, W = map(int, input().split())
v, w = [], []

dp = [0] * (W+1)  # 容量に対してDP
for i in range(N):
    v, w = map(int, input().split())
    for j in range(W, w-1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(max(dp))
