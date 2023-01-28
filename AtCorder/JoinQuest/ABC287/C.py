N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
 
if M != N - 1:
    print("No")
    exit()
 
for i in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
 
 
# 深さ優先探索の初期化
visited = [0] * (N + 1)
S = list() # スタック S を定義
visited[1] += 1
S.append(1) 
 
# 深さ優先探索
while len(S) >= 1:
    pos = S.pop() # S の先頭を調べ、これを取り出す
    for nex in G[pos]:
        if visited[nex] == False:
            visited[nex] = True
            S.append(nex) # S に nex を追加
 
answer = True
 
# 連結判定
for i in range(1, N + 1):
    if visited[i] == False:
        answer = False
        break


if answer:
    for i in range(1, N+1):
        if len(G[i]) > 2:
            print("No")
            exit()
    print("Yes")
else:
    print("No")