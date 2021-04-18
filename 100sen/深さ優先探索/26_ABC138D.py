"""
https://atcoder.jp/contests/abc138/tasks/abc138_d
カウントを記録しておいて、最後に子ノードに伝播する
"""

# class Node:
#     def __init__(self):
#         self.__count = 0
#         self.__children = []
#         self.__children_append = self.__children.append

#     def add_child(self, node):
#         self.__children_append(node)

#     def add_count(self, num):
#         self.__count += num
#         for child in self.__children:
#             child.add_count(num)

#     @property
#     def count(self):
#         return self.__count


# def main():
#     n, q = map(int, input().split())
#     node_map = {i + 1: Node() for i in range(n)}

#     for _ in range(n-1):
#         a, b = map(int, input().split())
#         node_map[a].add_child(node_map[b])

#     for _ in range(q):
#         p, x = map(int, input().split())
#         node_map[p].add_count(x)

#     results = [str(n.count) for n in node_map.values()]
#     print(' '.join(results))


# main()

from collections import deque


def main():
    N, Q = map(int, input().split())

    paths = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        paths[a].append(b)
        paths[b].append(a)  # why need ?

    counter = [0] * (N+1)
    for _ in range(Q):
        n, x = map(int, input().split())
        counter[n] += x

    queue = deque()
    queue.append(1)
    visited = [False] * (N+1)
    while queue:
        now = queue.pop()
        visited[now] = True

        for next in paths[now]:
            if visited[next]:   # why need ?
                continue        # why need ?
            counter[next] += counter[now]
            queue.append(next)

    print(*counter[1:])


main()
