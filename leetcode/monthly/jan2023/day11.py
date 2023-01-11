from collections import defaultdict


class Solution:
    # TODO: Worth coming back and figuring this out
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        # check if an apple exists
        has_apple = False

        for apple in hasApple:
            if apple:
                has_apple = True
                break

        if not has_apple:
            return 0

        # build the graph
        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        visited = set()

        def dfs(node: int) -> int:
            visited.add(node)

            res = 0

            for child in graph[node]:
                if child not in visited:
                    res += dfs(child)

            if (res > 0 or hasApple[node]) and node != 0:
                res += 2

            return res

        return dfs(0)
