N = int(input())
P = [0] * N  # 0番目は捨て

# 数字 i の約数組み合わせ総数
# 例：12 = (1,12)(2,6)(3,4)(4,3)(6,2)(12,1) の6パターン
# 組み合わせの左側のみをカウントすれば組み合わせ総数を出せる
for i in range(1, N):
    for j in range(i, N, i):
        P[j] += 1

ans = 0
for ab in range(1, N):
    cd = N - ab
    ans += P[ab] * P[cd]
print(ans)
