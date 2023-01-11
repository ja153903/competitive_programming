from typing import List, Self
from collections import defaultdict


class SparseVector:
    def __init__(self, nums: List[int]):
        self.sparse_vec = defaultdict(int)

        for i, val in enumerate(nums):
            self.sparse_vec[i] = val

    def dotProduct(self, vec: Self) -> int:
        this = self.sparse_vec
        other = vec.sparse_vec

        res = 0

        for key, value in this.items():
            if key in other:
                res += value * other[key]

        return res
