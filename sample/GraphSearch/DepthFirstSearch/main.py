from typing import List

# input
vertex_num = 8  # 頂点数
graph: List[List]= [
  [5],
  [3, 6],
  [5, 7],
  [0, 7],
  [1, 2, 6],
  [],
  [7],
  [0]
]
# output
route: List[int] = []


def dfs(current_num: int, graph_list: List[List], seen: List[bool]):
  seen[current_num] = True
  for next_num in graph_list[current_num]:
    if seen[next_num] == True:
      continue
    route.append(next_num)
    dfs(next_num, graph_list, seen)

def main():
  seen: List[bool] = [False] * vertex_num
  for i in range(vertex_num):
    if seen[i] == True:
      continue
    route.append(i)
    dfs(i, graph, seen)
  print(route)


main()
