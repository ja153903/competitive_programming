from collections import Counter, defaultdict


class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        def dfs(node: int) -> Counter:
            cnt = Counter()

            if node not in visited:
                cnt[labels[node]] += 1

                visited.add(node)

                # the idea with this solution is that at every level of the tree
                # we have built up a series of Counter objects that we can update
                # to get the updated count from the subtrees
                # this means that the leaves of the tree will have the smallest possible counter
                # and the counter bubbles up and becomes larger.
                for child in graph.get(node, []):
                    cnt += dfs(child)

                res[node] = cnt[labels[node]]

            return cnt

        res = [0] * n
        graph = defaultdict(list)
        visited = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        dfs(0)

        return res
