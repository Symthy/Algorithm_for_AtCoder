"""
プリム法
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_A&lang=jp

入力例
5
-1 2 3 1 -1
2 -1 -1 4 -1
3 -1 -1 1 1
1 4 1 -1 3
-1 -1 1 3 -1
"""


from heapq import heapify, heappop, heappush


def main():
    # 頂点数 n
    n = int(input())

    adjacency_matrix = []   # 隣接行列のリスト
    for _ in range(n):
        row = list(map(int, input().split()))
        adjacency_matrix.append([(cost, i) for i, cost in enumerate(row) if cost != -1])
    visited_vertex = [False] * n
    connect_count = 0
    que = [(0, 0)]    # (cost, vertex_index)
    heapify(que)
    total_cost = 0
    while True:
        cost, i = heappop(que)
        if visited_vertex[i]:
            continue

        visited_vertex[i] = True
        connect_count += 1
        total_cost += cost

        # 新たに繋げたノードから行けるところをエンキュー
        for tup in adjacency_matrix[i]:
            heappush(que, tup)

        if connect_count >= n:
            break
    print(total_cost)
    return
