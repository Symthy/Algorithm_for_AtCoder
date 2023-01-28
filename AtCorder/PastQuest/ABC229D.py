from collections import deque
 
S = list(input())
K = int(input())
period_que = deque([-1] * K)
before_period = -1

memo = []

maxLen = 0
for i in range(len(S)):
    if S[i] == ".":
        period_que.append(i)
        before_period = period_que.popleft()
    maxLen = max(i - before_period, maxLen)

print(maxLen)

# 取り出したperiodの位置と、入れるperiodの位置の差が長さになる
# deque の -1 が肝