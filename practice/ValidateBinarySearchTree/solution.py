from typing import List

from ValidateBinarySearchTree.util.tree_node import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        left_node: TreeNode = root.left
        if root.left is not None:
            if not root.val > left_node.val:
                return False
            if not isChildNodeValidBST(left_node, [supplyJudgeUpperNodeLargeValFunc(root.val)]):
                return False
        right_node: TreeNode = root.right
        if root.right is not None:
            if not root.val < right_node.val:
                return False
            if not isChildNodeValidBST(right_node, [supplyJudgeUpperNodeSmallValFunc(root.val)]):
                return False
        return True


def isChildNodeValidBST(current_node: TreeNode, compare_upper_node_funcs: List[Callable]) -> bool:
    left_node: TreeNode = current_node.left
    if left_node is not None:
        if not current_node.val > left_node.val:
            return False
        for compare_func in compare_upper_node_funcs:
            if not compare_func(left_node.val):
                return False
        if not isChildNodeValidBST(
                left_node, compare_upper_node_funcs + [supplyJudgeUpperNodeLargeValFunc(current_node.val)]):
            return False
    right_node: TreeNode = current_node.right
    if right_node is not None:
        if not current_node.val < right_node.val:
            return False
        for compare_func in compare_upper_node_funcs:
            if not compare_func(right_node.val):
                return False
        if not isChildNodeValidBST(
                right_node, compare_upper_node_funcs + [supplyJudgeUpperNodeSmallValFunc(current_node.val)]):
            return False
    return True


def supplyJudgeUpperNodeLargeValFunc(upper_node_val: int):
    return lambda current_node_val: upper_node_val > current_node_val


def supplyJudgeUpperNodeSmallValFunc(upper_node_val: int):
    return lambda current_node_val: upper_node_val < current_node_val
