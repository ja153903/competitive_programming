from collections import deque, defaultdict
from typing import Optional, DefaultDict

from leetcode.data_structures.trees import TreeNode


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []

        result: DefaultDict[int, list[TreeNode]] = defaultdict(list)

        queue = deque()
        queue.append((root, 0))

        while queue:
            node, value = queue.popleft()

            result[value].append(node)

            if node.left:
                queue.append((node.left, value - 1))

            if node.right:
                queue.append((node.right, value + 1))

        return [
            [v.val for v in value]
            for _, value in sorted(list(result.items()), key=lambda kv: kv[0])
        ]
