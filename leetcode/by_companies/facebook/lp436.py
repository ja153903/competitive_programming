from collections import deque

DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return self.bfs(grid, i, j)

        return 0

    def bfs(self, grid: list[list[int]], row: int, col: int) -> int:
        queue = deque()
        queue.append((row, col))

        visited = set()
        visited.add((row, col))

        res = 0

        while queue:
            r, c = queue.popleft()

            grid[r][c] = 0

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if (nr, nc) in visited:
                    continue

                if (
                    nr < 0
                    or nc < 0
                    or nr >= len(grid)
                    or nc >= len(grid[0])
                    or grid[nr][nc] != 1
                ):
                    res += 1
                else:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        return res
