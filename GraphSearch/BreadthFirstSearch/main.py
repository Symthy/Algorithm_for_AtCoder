from typing import List
import queue

# input
vertex_num = 9  # 頂点数
graph: List[List] = [
    [1, 2, 4],
    [0, 3, 4, 8],
    [5],
    [1, 7, 8],
    [0, 1, 8],
    [2, 6, 8],
    [5, 7],
    [3, 6],
    [1, 3, 4, 5]
]
# output
route: List[int] = []


def bfs(graph_list: List[int], start: int):
  dist: List[int] = [-1] * vertex_num
  dist[start] = 0
  next_nodes_que = queue.Queue()
  next_nodes_que.put(start)
  while not next_nodes_que.empty():
    node_index: int = next_nodes_que.get()
    for next_node_index in graph_list[node_index]:
      if dist[next_node_index] != -1:
        continue
      dist[next_node_index] = dist[node_index] + 1
      next_nodes_que.put(next_node_index)
  return dist


def main():
  dist: List[int] = bfs(graph, 0)
  for i in range(len(dist)):
    print(str(i) + " : " + str(dist[i]))


main()
