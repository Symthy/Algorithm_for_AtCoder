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

    is_exist_negative_cycle: bool = False
    vertex_cost_dict: Dict[int, int] = {i: INF for i in range(vertex_num)}
    vertex_cost_dict = {start_num: 0}
    for i in range(vertex_num):
        is_update = False
        for v in range(vertex_num):
            if vertex_cost_dict[v] == 0:
                continue
            for e in graph[v]:
                # 緩和処理
                if choose_min(vertex_cost_dict[e.to], vertex_cost_dict[v] + e.weight):
                    is_update = True
                    vertex_cost_dict[e.to] = vertex_cost_dict[v] + e.weight

        if not is_update:
            # 更新が行われなかったら終了(最短経路が求まっている)
            break
        if i == vertex_num - 1 and is_update:
            # 頂点数回目で更新が行われた場合は負閉路
            is_exist_negative_cycle = True

    # result output
    if is_exist_negative_cycle:
        print('Negative Cycle')
        return
    for v in range(vertex_num):
        if vertex_cost_dict[v] < INF:
            print(vertex_cost_dict[v])
        else:
            print('INF')


main()
