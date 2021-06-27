from collections import defaultdict


class UnionFind():
    def __init__(self, node_num):
        self.node_num = node_num
        self.parents = [-1] * node_num

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, v1, v2):
        v1 = self.find(v1)
        v2 = self.find(v2)

        if v1 == v2:
            return

        if self.parents[v1] > self.parents[v2]:
            vertex1, vertex2 = vertex2, vertex1

        self.parents[v1] += self.parents[v2]
        self.parents[v2] = v1

    def size(self, v):
        return -self.parents[self.find(v)]

    def same(self, v1, v2):
        return self.find(v1) == self.find(v2)

    def members(self, v):
        root = self.find(v)
        return [i for i in range(self.node_num) if self.find(i) == root]

    def roots(self):
        return [i for i, v in enumerate(self.parents) if v < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.node_num):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
