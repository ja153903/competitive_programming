import sys


class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        """
        Let's use 2 DFS searches for this problem
        """

        dists1, dists2 = {}, {}

        i, dist = node1, 0
        while i >= 0 and i not in dists1:
            dists1[i] = dist
            dist += 1
            i = edges[i]

        i, dist = node2, 0
        while i >= 0 and i not in dists2:
            dists2[i] = dist
            dist += 1
            i = edges[i]

        min_dist = sys.maxsize
        result = -1

        for node in range(len(edges)):
            dist_from_node1 = dists1.get(node, -1)
            dist_from_node2 = dists2.get(node, -1)

            if (
                min(dist_from_node1, dist_from_node2) >= 0
                and max(dist_from_node1, dist_from_node2) < min_dist
            ):
                min_dist = max(dist_from_node1, dist_from_node2)
                result = node

        return result
