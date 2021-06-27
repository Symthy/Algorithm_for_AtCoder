"""
単一始点最短経路
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja
"""
from heapq import heappop, heappush
from typing import Dict, List, TypeVar

INF = float('inf')


class Edge:
    def __init__(self, to: int, weight: int):
        self.to: int = to
        self.weight: int = weight


def dijkstra():
    # V:頂点数, E:辺数, r:始点
    print('入力(頂点数 辺数 始点):')
    V, E, start_index = map(int, input().split())
    # s,t:辺(有向), d:重み

    graph: List[List[Edge]] = []
    for i in range(V):
        graph.append([])
    print('頂点(from) 頂点(to) 重み:')
    for i in range(E):
        s, t, w = map(int, input().split())
        e = Edge(t, w)
        graph[s].append(e)

    que = []
    heappush(que, (0, start_index))  # used_vertex_listの代わりにもなる
    vertex_cost: Dict[int, int] = {i: INF for i in range(V)}
    vertex_cost[start_index] = 0
    while que:
        # 使用済みでない最小コストの頂点を探す
        min_cost, min_vertex_index = heappop(que)

        # min_vertex を始点に緩和処理
        for e in graph[min_vertex_index]:
            if vertex_cost[e.to] > min_cost + e.weight:
                vertex_cost[e.to] = min_cost + e.weight
                heappush(que, (vertex_cost[e.to], e.to))

    for cost in vertex_cost.values():
        if cost == INF:
            print("INF")
        else:
            print(cost)


dijkstra()
