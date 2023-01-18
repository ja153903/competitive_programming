class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        def dfs(row: int, col: int) -> int:
            if (
                row < 0
                or col < 0
                or row >= len(grid)
                or col >= len(grid[0])
                or grid[row][col] != 1
            ):
                return 1

            if (row, col) in visited:
                return 0

            visited.add((row, col))

            return (
                dfs(row + 1, col)
                + dfs(row - 1, col)
                + dfs(row, col + 1)
                + dfs(row, col - 1)
            )

        visited = set()
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return dfs(row, col)

        return 0
