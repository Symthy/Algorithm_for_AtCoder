"""
クラスカル法
https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A&lang=ja
入力例：
6 9
0 1 1
0 2 3
1 2 1
1 3 7
2 4 1
1 4 3
3 4 1
3 5 1
4 5 6
"""


class UnionFind():
    def __init__(self, node_num):
        self.node_num = node_num
        self.parents = [-1] * node_num

    def find(self, v):
        if self.parents[v] < 0:
            return v
        else:
            self.parents[v] = self.find(self.parents[v])
            return self.parents[v]

    def union(self, v1, v2):
        v1 = self.find(v1)
        v2 = self.find(v2)

        if v1 == v2:
            return

        if self.parents[v1] > self.parents[v2]:
            vertex1, vertex2 = vertex2, vertex1

        self.parents[v1] += self.parents[v2]
        self.parents[v2] = v1

    def same(self, v1, v2):
        return self.find(v1) == self.find(v2)


def main():
    V, E = map(int, input().split())
    uf = UnionFind(V)

    # 1の過程
    edges = []
    for _ in range(E):
        s, t, w = map(int, input().split())
        edges.append((w, s, t))
    edges.sort()

    # 2の過程
    cost = 0
    for edge in edges:
        w, s, t = edge
        if not uf.same(s, t):
            cost += w
            uf.union(s, t)
    print(cost)
    return
