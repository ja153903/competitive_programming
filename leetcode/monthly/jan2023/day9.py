from typing import Optional

from leetcode.data_structures.trees import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def preorder(node: Optional[TreeNode], result: list[int]):
            if node:
                result.append(node.val)
                preorder(node.left, result)
                preorder(node.right, result)

        result = []
        preorder(root, result)

        return result
