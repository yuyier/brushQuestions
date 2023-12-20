# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from tree_node import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        result_bool = True
        return self.isSymmetricTree(root.left, root.right, result_bool)

    def isSymmetricTree(self, tree_node1: Optional[TreeNode], tree_node2: Optional[TreeNode],
                        result_bool: bool) -> bool:
        if tree_node1 and tree_node2:
            result_bool = result_bool and tree_node1.val == tree_node2.val
        elif (tree_node1 and not tree_node2) or (not tree_node1 and tree_node2):
            result_bool = result_bool and False
        else:
            return result_bool and True
        return result_bool and self.isSymmetricTree(tree_node1.left, tree_node2.right,
                                                    result_bool) and self.isSymmetricTree(tree_node1.right,
                                                                                          tree_node2.left, result_bool)
