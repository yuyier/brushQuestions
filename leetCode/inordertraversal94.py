from typing import Optional, List

from tree_node import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list_result = []
        return self.returnInorderList(list_result, root)

    def returnInorderList(self, list_result: List, tree_node: Optional[TreeNode]) -> List[int]:
        if tree_node:
            self.returnInorderList(list_result, tree_node.left)
            list_result.append(tree_node.val)
            self.returnInorderList(list_result, tree_node.right)
        return list_result
