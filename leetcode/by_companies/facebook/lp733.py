from collections import deque

DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]]


class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        if image[sr][sc] == color:
            return image

        orig = image[sr][sc]

        queue = deque()
        queue.append((sr, sc))

        while queue:
            r, c = queue.popleft()

            image[r][c] = color

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc

                if (
                    nr < 0
                    or nc < 0
                    or nr >= len(image)
                    or nc >= len(image[0])
                    or image[nr][nc] != orig
                ):
                    continue

                queue.append((nr, nc))

        return image
