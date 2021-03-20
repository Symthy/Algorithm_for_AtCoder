"""
ダイクストラ
・始点
"""

from typing import Dict, List, TypeVar

INF = float('inf')


class Edge:
    def __init__(self, to: int, weight: int):
        self.to: int = to
        self.weight: int = weight


# 緩和処理
def choose_min(vertex1: int, vertex2: int) -> int:
    if vertex1 > vertex2:
        return False
    return True


def output(vertex_num: int, vertex_cost: Dict[int, int]):
    for v in range(vertex_num):
        if (vertex_cost[v] < INF):
            print(str(v) + ': ' + str(vertex_cost[v]))
        else:
            print(str(v) + ': INF')


def main():
    print('入力(頂点数 辺数 始点):')
    vertex, edge, start = input()
    vertex_num = int(vertex)
    edge_num = int(edge)
    start_num = int(start)

    print('グラフ入力')
    graph: List[List[Edge]] = []
    for i in range(vertex_num):
        graph.append([])
    for i in range(edge_num):
        print('頂点(from) 頂点(to) 重み:')
        v1, v2, w = input()
        e = Edge(int(v2), int(w))
        graph[v1].append(e)

    # ダイクストラ
    used_vertex: Dict[int, bool] = {i: False for i in range(vertex_num)}
    vertex_cost: Dict[int, int] = {i: INF for i in range(vertex_num)}
    vertex_cost[start_num] = 0

    for i in range(vertex):
        # 使用済みでない最小コストの頂点を探す
        min_cost = INF
        min_vertex = -1
        for v, cost in vertex_cost.items():
            if not v in used_vertex and cost < min_cost:
                min_cost = vertex_cost[v]
                min_vertex = v

        if min_vertex == -1:
            break

        # min_vertex を始点に緩和処理
        for e in graph[min_vertex]:
            if choose_min(vertex_cost[e.to], vertex_cost[min_vertex] + e.weight):
                vertex_cost[e.to] = vertex_cost[v] + e.weight
        used_vertex[min_vertex] = True

    output(vertex_num, vertex_cost)
