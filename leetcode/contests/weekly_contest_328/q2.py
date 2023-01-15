from typing import List

import numpy as np


class Solution:
    def rangeAddQueries_tle(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0 for _ in range(n)] for _ in range(n)]

        for query in queries:
            row1, col1, row2, col2 = query

            for row in range(row1, row2 + 1):
                for col in range(col1, col2 + 1):
                    mat[row][col] += 1

        return mat

    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = np.array([[0 for _ in range(n)] for _ in range(n)])

        for query in queries:
            row1, col1, row2, col2 = query

            mat[row1 : row2 + 1, col1 : col2 + 1] += 1

        return list(mat)
