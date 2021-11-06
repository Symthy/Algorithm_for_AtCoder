import sys

# デフォルト1000だから増やさないと失敗する
sys.setrecursionlimit(300000)


def dfs(cur, pre, ans, G):
    ans.append(cur)
    for nxt in G[cur]:
        if nxt != pre:
            dfs(nxt, cur, ans, G)
            ans.append(cur)


def main():
    N = int(input())
    G = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    for i in range(N+1):
        G[i].sort()

    ans = []
    dfs(1, -1, ans, G)
    print(' '.join(list(map(str, ans))))


main()
