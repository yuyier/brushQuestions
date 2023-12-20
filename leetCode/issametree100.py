from typing import Optional, List

from tree_node import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return_result = True
        return self.theSameTree(p, q, return_result)

    def theSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode], return_result: bool) -> bool:
        if (p and not q) or (not p and q):
            return_result = return_result and False
        if p and q:
            return_result = return_result and (p.val == q.val) and self.theSameTree(p.left, q.left,
                                                                                    return_result) and self.theSameTree(
                p.right, q.right, return_result)
        return return_result
