from collections import defaultdict, deque


class UnionFind:
    """
    Typically we'll reach for Union Find
    algorithms when we're concerned about operations
    on connected components
    """

    def __init__(self, n: int) -> None:
        self.number_of_nodes = n
        self.parents = list(range(self.number_of_nodes))
        self.ranks = [0] * self.number_of_nodes

    def union(self, u: int, v: int) -> None:
        parent_of_u = self.find(u)
        parent_of_v = self.find(v)

        if parent_of_u == parent_of_v:
            return

        if self.ranks[parent_of_u] < self.ranks[parent_of_v]:
            self.parents[parent_of_u] = parent_of_v
            self.ranks[parent_of_v] += 1
        else:
            self.parents[parent_of_v] = parent_of_u
            self.ranks[parent_of_u] += 1

    def find(self, node: int) -> int:
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])

        return self.parents[node]


def kahn(n: int, edges: list[list[int]]):
    """
    This algorithm can be used to solve problems
    whose solution involves topological sort

    Use this template to solve various kahn problems
    """

    graph = defaultdict(list)
    indegree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque()

    for node, count in enumerate(indegree):
        if count == 0:
            queue.append(node)

    while queue:
        front = queue.popleft()

        # You can do something with this information around here

        for child in graph[front]:
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)
