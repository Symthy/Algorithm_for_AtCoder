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
    vertex_num, edge_num, start_num = map(int, input().split())

    print('グラフ入力')
    graph: List[List[Edge]] = []
    for i in range(vertex_num):
        graph.append([])
    for i in range(edge_num):
        # print('頂点(from) 頂点(to) 重み:')
        v1, v2, w = map(int, input().split())
        e = Edge(v2, w)
        graph[v1].append(e)

    # ダイクストラ
    used_vertex: Dict[int, bool] = {i: False for i in range(vertex_num)}
    vertex_index_cost: Dict[int, int] = {i: INF for i in range(vertex_num)}
    vertex_index_cost[start_num] = 0

    for _ in range(vertex_num):
        # 使用済みでない最小コストの頂点を探す
        # ヒープキュー使えば早くなる。要素追加/最小要素取り出し:O(logN)
        min_cost = INF
        min_vertex_index = -1
        for v_index, cost in vertex_index_cost.items():
            if not v_index in used_vertex and cost < min_cost:
                min_vertex_index = v_index
                min_cost = vertex_index_cost[min_vertex_index]
        if min_vertex_index == -1:
            break

        # min_vertex を始点に緩和処理
        for e in graph[min_vertex_index]:
            if choose_min(vertex_index_cost[e.to], min_cost + e.weight):
                vertex_index_cost[e.to] = min_cost + e.weight
        used_vertex[min_vertex_index] = True

    output(vertex_num, vertex_index_cost)


main()
