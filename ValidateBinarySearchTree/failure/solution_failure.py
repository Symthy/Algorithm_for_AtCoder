# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from ValidateBinarySearchTree.util.tree_node import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ret = True

        if root.left is not None:
            if root.val > root.left.val:
                ret = ret and self.isChildNodeValidBST(
                    root.val, root.left, lambda upper_node_val, current_node_val: upper_node_val > current_node_val)
            else:
                return False
        if root.right is not None:
            if root.val < root.right.val:
                ret = ret and self.isChildNodeValidBST(
                    root.val, root.right, lambda upper_node_val, current_node_val: upper_node_val < current_node_val)
            else:
                return False
        return ret

    def isChildNodeValidBST(self, rootVal: int, child_node: TreeNode, judgeAsUpperNodeFunc):
        ret = True
        upper_node_vals: List[int] = [rootVal]
        left_node: TreeNode = child_node.left
        if left_node is not None:
            if not judgeAsUpperNodeFunc(rootVal, left_node.val):
                return False
            if not child_node.val > left_node.val:
                return False
            else:
                ret = ret and self.isGrandChildNodeValidBST(
                    upper_node_vals + [child_node.val], left_node, getjudgeAsUpperNodeListFunc(judgeAsUpperNodeFunc))
        if not ret:
            return False
        right_node: TreeNode = child_node.right
        if right_node is not None:
            if not judgeAsUpperNodeFunc(rootVal, right_node.val):
                return False
            if not child_node.val < right_node.val:
                return False
            else:
                ret = ret and self.isGrandChildNodeValidBST(
                    upper_node_vals + [child_node.val], right_node, getjudgeAsUpperNodeListFunc(judgeAsUpperNodeFunc))
        return ret

    def isGrandChildNodeValidBST(self, upper_node_vals: List[int], current_node: TreeNode,
                                 judgeAsUpperNodeListFunc) -> bool:
        ret = True
        left_node: TreeNode = current_node.left
        if left_node is not None:
            if not judgeAsUpperNodeListFunc(upper_node_vals, left_node.val):
                return False
            if not current_node.val > left_node.val:
                return False
            else:
                ret = ret and self.isGrandChildNodeValidBST(
                    upper_node_vals + [current_node.val], left_node, judgeAsUpperNodeListFunc)
        if not ret:
            return False
        right_node: TreeNode = current_node.right
        if current_node.right is not None:
            if not judgeAsUpperNodeListFunc(upper_node_vals, right_node.val):
                return False
            if not current_node.val < right_node.val:
                return False
            else:
                ret = ret and self.isGrandChildNodeValidBST(
                    upper_node_vals + [current_node.val], right_node, judgeAsUpperNodeListFunc)
        return ret


def getjudgeAsUpperNodeListFunc(judgeAsUpperNodeFunc):
    return lambda upperNodeVals, currentNodeVal: compareUpperNodesVal(upperNodeVals, currentNodeVal,
                                                                      judgeAsUpperNodeFunc)


def compareUpperNodesVal(upperNodeVals, currentNodeVal, judgeAsUpperNodeFunc):
    for i in range(len(upperNodeVals)):
        if not judgeAsUpperNodeFunc(upperNodeVals[i], currentNodeVal):
            return False
    return True
