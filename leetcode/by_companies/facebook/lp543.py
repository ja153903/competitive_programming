from typing import Optional

from leetcode.data_structures.trees import TreeNode


class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # to find the diameter of a binary tree, we need to find the longest path from one node to another
        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left, right = depth(node.left), depth(node.right)

            self.res = max(self.res, left + right)

            return max(left, right) + 1

        depth(root)

        return self.res
