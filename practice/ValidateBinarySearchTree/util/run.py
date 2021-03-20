from typing import List

from ValidateBinarySearchTree.failure.solution_failure import Solution
from ValidateBinarySearchTree.util.tree_node import TreeNode

input: str = input()
array_binary_tree: List[str] = input.split(',')

node_list = [TreeNode() for _ in range(len(array_binary_tree))]
root = node_list[0]
j = 0
k = 0
for i in range(len(node_list)):
    if array_binary_tree[i] == 'null':
        continue
    node_list[i].val = int(array_binary_tree[i])
    if i == 0:
        continue
    if i % 2 != 0:
        node_list[j].left = node_list[i]
        k += 1
    if i % 2 == 0:
        node_list[j].right = node_list[i]
        k += 1
    if k == 2:
        k = 0
        j += 1

sol = Solution()
print(sol.isValidBST(root))
