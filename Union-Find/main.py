from typing import List

class UnionFind:
  parent_node_indexes: List[int] = []
  child_node_counts: List[int] = []

  def __init__(self, num: int):
    self.parent_node_indexes = [-1] * num
    self.child_node_counts = [1] * num

  # 根を求める＆経路圧縮
  def resolve_root_index(self, node_index: int) -> int:
    if self.parent_node_indexes[node_index] == -1:
      return node_index
    else:
      self.parent_node_indexes[node_index] = self.resolve_root_index(
          self.parent_node_indexes[node_index])
      return self.parent_node_indexes[node_index]

  def is_same(self, node_index_1: int, node_index_2: int) -> bool:
    return self.resolve_root_index(node_index_1) == self.resolve_root_index(node_index_2)

  def unite(self, node_index_1: int, node_index_2: int) -> bool:
    root_index_1 = self.resolve_root_index(node_index_1)
    root_index_2 = self.resolve_root_index(node_index_2)
    if root_index_1 == root_index_2:
      return False
    # 併合
    if self.child_node_counts[root_index_1] < self.child_node_counts[root_index_2]:
      self.parent_node_indexes[root_index_2] = root_index_1
      self.child_node_counts[root_index_1] += self.child_node_counts[root_index_2]
    else:
      self.parent_node_indexes[root_index_1] = root_index_2
      self.child_node_counts[root_index_2] += self.child_node_counts[root_index_1]
    return True

  # nodeを含むグループのサイズ
  def get_belongs_group_size(self, node_index: int) -> int:
    return self.child_node_counts[self.resolve_root_index(node_index)]


def main():
  vertex_num = 7 # 頂点数
  uf = UnionFind(vertex_num)  # [0, 1, 2, 3, 4, 5, 6]
  print("親ノード：" + str(uf.parent_node_indexes))
  print("子ノード数：" + str(uf.child_node_counts))
  print("------")
  uf.unite(1, 2)
  print("親ノード：" + str(uf.parent_node_indexes))
  print("子ノード数：" + str(uf.child_node_counts))
  print("------")
  uf.unite(2, 3)
  print("親ノード：" + str(uf.parent_node_indexes))
  print("子ノード数：" + str(uf.child_node_counts))
  print("------")
  uf.unite(5, 6)
  print("親ノード：" + str(uf.parent_node_indexes))
  print("子ノード数：" + str(uf.child_node_counts))
  print(uf.is_same(1, 3))
  print(uf.is_same(2, 5))
  print("------")
  uf.unite(1, 6)
  print("親ノード：" + str(uf.parent_node_indexes))
  print("子ノード数：" + str(uf.child_node_counts))
  print(uf.is_same(2, 5))

main()
