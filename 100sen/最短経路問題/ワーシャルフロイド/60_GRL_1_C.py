"""
全点対間最短経路
グラフの全ての頂点の間の最短路を見つける
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C&lang=ja
"""

from math import isinf
from typing import List, TypeVar

INF = float('inf')


def main():
    # V:頂点数、E:辺数
    V, E = map(int, input().split())

    # graph: List[List] = []
    # for i in range(V):
    #     row: List = []
    #     for j in range(V):
    #         if i == j:
    #             row.append(0)
    #         else:
    #             row.append(INF)
    #     graph.append(row)
    graph: List[List] = [[float('inf') for i in range(V)] for j in range(V)]

   # s:始点, t:終点, w:重み
    for _ in range(E):
        s, t, w = map(int, input().split())
        graph[s][t] = w
    for i in range(V):
        graph[i][i] = 0

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    # output
    # output: List[str] = []
    # for i in range(V):
    #     if any(((cost < 0 for cost in graph[i]))):
    #         print("NEGATIVE CYCLE")
    #         break
    #     row: List = []
    #     for j in range(V):
    #         if graph[i][j] == INF:
    #             row.append('INF')
    #         else:
    #             row.append(str(graph[i][j]))
    #     output.append(' '.join(row))
    # for r in output:
    #     print(r)
    for i in range(V):
        if graph[i][i] < 0:
            print('NEGATIVE CYCLE')
            exit()

    for graph_row in graph:
        print(' '.join(('INF' if isinf(elem) else str(elem) for elem in graph_row)))


main()
