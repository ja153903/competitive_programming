class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def dfs(row: int, col: int) -> int:
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != 1:
                return 0

            grid[row][col] = 0

            return (
                1
                + dfs(row + 1, col)
                + dfs(row - 1, col)
                + dfs(row, col + 1)
                + dfs(row, col - 1)
            )

        rows, cols = len(grid), len(grid[0])
        res = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    res = max(res, dfs(row, col))

        return res
