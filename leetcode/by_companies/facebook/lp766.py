class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        """
        A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
        """

        rows, cols = len(matrix), len(matrix[0])

        # go across the first row
        for col in range(cols):
            prev = None
            for r, c in zip(range(rows), range(col, cols)):
                if prev is None:
                    prev = matrix[r][c]

                if prev != matrix[r][c]:
                    return False

        # go down the first column
        for row in range(1, rows):
            prev = None
            for r, c in zip(range(row, rows), range(cols)):
                if prev is None:
                    prev = matrix[r][c]

                if prev != matrix[r][c]:
                    return False

        return True
