import heapq
from collections import defaultdict


class Solution:
    def longestPath(self, parent: list[int], s: str) -> int:
        """
        we should build a graph based on the list of parents that we're given
        Turn the above list of parents into a graph
        [-1, 0, 0, 1, 1, 2] =>
        {0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3: [1], 4: [1], 5: [2]}
        """
        graph = defaultdict(list)

        for i, value in enumerate(parent):
            if value >= 0:
                graph[value].append(i)

        def dfs(node: int) -> int:
            candidates = [0]
            for child in graph[node]:
                current = dfs(child)
                if s[child] != s[node]:
                    candidates.append(current)

            candidates = heapq.nlargest(2, candidates)
            res[0] = max(res[0], sum(candidates) + 1)
            return max(candidates) + 1

        res = [0]
        dfs(0)

        return res[0]
