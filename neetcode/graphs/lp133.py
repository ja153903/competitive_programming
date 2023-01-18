from typing import Self
from collections import deque, defaultdict


class Node:
    def __init__(self, val: int = 0, neighbors: list[Self] | None = None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        if node is None:
            return None

        # when we're cloning a graph
        # we really just want to iterate over
        # every node
        copies = defaultdict()
        visited = set()
        queue = deque()

        head = Node(val=node.val)

        queue.append((node, head))
        visited.add(node.val)
        copies[node.val] = head

        while queue:
            orig, clone = queue.popleft()

            for nei in orig.neighbors:
                if nei.val in visited:
                    clone.neighbors.append(copies[nei.val])
                else:
                    nei_clone = Node(val=nei.val)
                    clone.neighbors.append(nei_clone)
                    queue.append((nei, nei_clone))
                    visited.add(nei.val)

                    copies[nei.val] = nei_clone

        return copies[node.val]
